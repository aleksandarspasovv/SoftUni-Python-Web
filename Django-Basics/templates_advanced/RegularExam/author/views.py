from django.shortcuts import redirect, render
from author.forms import AuthorForm
from author.models import Author


def create_author_profile_view(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to dashboard after creation
    else:
        form = AuthorForm()
    return render(request, 'author/create-author.html', {'form': form})


def author_details_view(request):
    author = Author.objects.first()  # Assuming one author for simplicity
    return render(request, 'author/details-author.html', {'author': author})


def edit_author_view(request):
    author = Author.objects.first()  # Assuming one author for simplicity
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author-details')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author/edit-author.html', {'form': form})


def delete_author_view(request):
    author = Author.objects.first()  # Assuming one author for simplicity
    if request.method == 'POST':
        author.delete()
        return redirect('home')  # Redirect to home page after deletion
    return render(request, 'author/delete-author.html', {'author': author})
