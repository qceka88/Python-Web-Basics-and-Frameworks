from .models import Profile, Note
from .forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm

from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if not find_profile():

        if request.method == 'GET':
            form = CreateProfileForm()
        else:
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home page')

        data = {
            'form': form,
        }

        return render(request, 'core/home-no-profile.html', data)
    else:
        notes = Note.objects.all()

        data = {
            'notes': notes,
        }

        return render(request, 'core/home-with-profile.html', data)


def add_note_page(request):
    form = CreateNoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home page')

    data = {
        'form': form,
        'add_note': True,
    }

    return render(request, 'notes/note-create.html', data)


def edit_note_page(request, pk):
    note = Note.objects.filter(pk=pk).get()
    form = EditNoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('home page')

    data = {
        'form': form,
        'note': note,
    }

    return render(request, 'notes/note-edit.html', data)


def delete_note_page(request, pk):
    note = Note.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteNoteForm(instance=note)
    else:
        note.delete()
        return redirect('home page')

    data = {
        'form': form,
        'note': note
    }

    return render(request, 'notes/note-delete.html', data)


def note_details_page(request, pk):
    note = Note.objects.filter(pk=pk).get()

    data = {
        'note': note,
    }

    return render(request, 'notes/note-details.html', data)


def profile_page(request):
    profile = Profile.objects.get()

    data = {
        'profile_name': profile.first_name + ' ' + profile.last_name,
        'profile_image': profile.image_url,
        'profile_age': profile.age,
        'notes_count': Note.objects.all().count(),
    }

    return render(request, 'profiles/profile.html', data)


def profile_delete(request):
    profile = find_profile()
    profile.delete()
    Note.objects.all().delete()
    return redirect('home page')


# helping_functions
def find_profile():
    try:
        return Profile.objects.all().first()
    except Profile.DoesNotExist:
        return None
