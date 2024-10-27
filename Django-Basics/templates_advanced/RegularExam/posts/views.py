from django.shortcuts import render, redirect, get_object_or_404
from author.models import Author
from posts.forms import PostForm
from posts.models import Post


def index_view(request):

    return render(request, 'index.html')


def create_post_view(request):

    author = Author.objects.first()
    if not author:

        return redirect('create-author-profile')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = author
            post.save()

            return redirect('dashboard')
    else:
        form = PostForm()

    return render(request, 'post/create-post.html', {'form': form})


def dashboard_view(request):
    posts = Post.objects.all()

    return render(request, 'dashboard.html', {'posts': posts})


def post_details_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'post/details-post.html', {'post': post})


def edit_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

            return redirect('post-details', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'post/edit-post.html', {'form': form, 'post': post})


def delete_post_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        post.delete()

        return redirect('dashboard')

    return render(request, 'post/delete-post.html', {'post': post})
