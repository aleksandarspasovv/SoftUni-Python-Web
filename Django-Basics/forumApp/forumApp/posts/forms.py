from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory

from forumApp.posts.mixins import DisabledRequiredFields
from forumApp.posts.models import Post, Comment


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        error_messages = {
            'title': {
                'required': '...',
                'max_length': 'Message too long',
            }
        }

    def clean_author(self):
        author = self.cleaned_data.get('author')

        if author[0] != author[0].upper():
            raise ValidationError("Author must be with a capital Letter")

        return author

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and content and title in content:
            raise ValidationError('tile cannot be included in the content')

        return cleaned_data

class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm, DisabledRequiredFields):
    disabled_fields = ('__all__', )
    pass



class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a post...',
            }
        )
    )

# class PostForm(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#     )
#
#     content = forms.CharField(
#         widget=forms.Textarea,
#     )
#
#     author = forms.CharField(
#         max_length=30,
#     )
#
#     created_at = forms.DateTimeField()
#
#     languages = forms.ChoiceField(
#         choices=LanguageChoice.choices
#     )


class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ('author', 'content',)

        labels = {
            'author': '',
            'content': '',
        }

        error_messages = {
            'author': {
                'required': 'Author name is required'
            },
            'content': {
                'required': 'Content is required'
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'form-control'
        })


CommentSetForm = formset_factory(CommentForm, extra=3)
