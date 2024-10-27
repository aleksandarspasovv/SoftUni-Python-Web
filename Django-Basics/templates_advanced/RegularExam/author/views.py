from django.shortcuts import redirect, render, get_object_or_404

from author.forms import AuthorForm
from author.models import Author


def create_author_profile_view(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AuthorForm()
    return render(request, 'author/create-author.html', {'form': form})


def author_details_view(request):
    author = Author.objects.first()

    if author is None:
        return render(request, 'author/details-author.html', {'author': None})

    return render(request, 'author/details-author.html', {'author': author})


def edit_author_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author-details', pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author/edit-author.html', {'form': form, 'author': author})


def delete_author_view(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == 'POST':
        author.delete()
        return redirect('home')

    return render(request, 'author/delete-author.html', {'author': author})