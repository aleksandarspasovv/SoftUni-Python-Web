# posts/views.py
from django.shortcuts import render, redirect, get_object_or_404

from author.models import Author
from posts.forms import PostForm
from posts.models import Post


# posts/views.py


def index_view(request):
    return render(request, 'index.html')  # Make sure 'index.html' exists in your templates directory


def create_post_view(request):
    # Check if an author exists
    author = Author.objects.first()  # Fetch the first author from the database
    if not author:
        # Redirect or show an error if no author exists
        return redirect('create-author-profile')  # Adjust to your URL name

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = author  # Associate with the existing author
            post.save()
            return redirect('dashboard')  # Redirect to dashboard after creation
    else:
        form = PostForm()

    return render(request, 'post/create-post.html', {'form': form})


def dashboard_view(request):
    posts = Post.objects.all()
    return render(request, 'dashboard.html', {'posts': posts})


def post_details_view(request, pk):  # Change id to pk
    post = get_object_or_404(Post, pk=pk)  # Use pk to fetch the post
    return render(request, 'post/details-post.html', {'post': post})


def edit_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-details', pk=post.pk)  # Redirect using pk
    else:
        form = PostForm(instance=post)
    return render(request, 'post/edit-post.html', {'form': form, 'post': post})


def delete_post_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('dashboard')
    return render(request, 'post/delete-post.html', {'post': post})
