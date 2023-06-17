from django.shortcuts import render, redirect

from online_library.library_web.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateBookForm, \
    EditBookForm
from online_library.library_web.models import Profile, Book


# TODO : FIX 3 ON ROW
# Create your views here.
def index(request):
    profile = find_profile()
    books = list(Book.objects.all())

    if profile:
        data = {
            'profile': profile.get(),
            'books': books,
        }
        return render(request, 'core/home-with-profile.html', data)
    else:
        if request.method == 'GET':
            form = CreateProfileForm()
        else:
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home page')

        data = {
            'form': form,
            'registered_user': True,
            'profile': profile,
        }

        return render(request, 'core/home-no-profile.html', data)


def add_book_page(request):
    if request.method == "GET":
        form = CreateBookForm()
    else:
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    data = {
        'form': form,
    }
    return render(request, 'books/add-book.html', data)


def edit_book_page(request, pk):
    book = Book.objects.filter(pk=pk).get()
    form = EditBookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('home page')
    data = {
        'form': form,
        'book': book,
    }

    return render(request, 'books/edit-book.html', data)


def details_book_page(request, pk):
    book = Book.objects.filter(pk=pk).get()

    data = {
        'book': book,
    }

    return render(request, 'books/book-details.html', data)


def delete_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    book.delete()
    return redirect('home page')


def profile_page(request):
    profile = Profile.objects.all().first()

    data = {
        'profile': profile,
    }

    return render(request, 'profiles/profile.html', data)


def profile_edit_page(request):
    profile = Profile.objects.all().first()

    form = EditProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('home page')

    data = {
        'form': form,
    }

    return render(request, 'profiles/edit-profile.html', data)


def profile_delete_page(request):
    profile = Profile.objects.all().first()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        profile.delete()
        return redirect('home page')

    data = {
        'form': form,
    }

    return render(request, 'profiles/delete-profile.html', data)


# helping functions
def find_profile():
    try:
        return Profile.objects.all()
    except Profile.DoesNotExist:
        return None
