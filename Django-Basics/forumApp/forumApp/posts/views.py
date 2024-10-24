from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from forumApp.posts.forms import PostCreateForm, PostDeleteForm, SearchForm, PostEditForm, CommentSetForm
from forumApp.posts.models import Post


class Index(View):
    def get(self, request, *args, **kwargs):
        context = {
            "dynamic_time": datetime.now(),
        }

        return render(request, 'common/index.html', context)


class IndexView(TemplateView):

    template_name = 'common/index.html'

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['common/index_logged.html']
        else:
            return ['common/index.html']

# def index(request):
#     post_form = modelform_factory(Post, fields=('title', 'author', 'content', 'languages'))
#
#     context = {
#         "my_form": post_form,
#     }
#
#     return render(request, 'common/index.html', context)


def dashboard(request):
    form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == "GET":
        if form.is_valid():
            query = form.cleaned_data['query']
            posts = posts.filter(title__icontains=query)

    context = {
        "posts": posts,
        "form": form,
    }

    return render(request, 'posts/dashboard.html', context)


def add_post(request):
    form = PostCreateForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        "form": form,
    }

    return render(request, 'posts/add-post.html', context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    if request.method == 'POTS':
        form = PostEditForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('dash')

    else:
        form = PostEditForm(instance=post)

    context = {
        'form': form,
        'post': post
    }
    return render(request, 'posts/edit-post.html', context)


def details_page(request, pk: int):
    post = Post.objects.get(pk=pk)
    formset = CommentSetForm(request.POST or None)

    if request.method == 'POST':
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(comit=False)
                    comment.post = post
                    comment.save()

            return redirect('details-post', pk=post.id)

    context = {
        "post": post,
        'formset': formset,
    }

    return render(request, 'posts/details-post.html', context)


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == "POST":
        post.delete()
        return redirect('dash')

    context = {
        "form": form,
        "post": post,
    }

    return render(request, 'posts/delete-post.html', context)