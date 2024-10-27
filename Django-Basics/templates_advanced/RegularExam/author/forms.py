# authors/forms.py
from django import forms

from author.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number', 'info', 'image_url']
        widgets = {
            'passcode': forms.PasswordInput(attrs={'placeholder': 'Enter 6 digits...'}),
        }
