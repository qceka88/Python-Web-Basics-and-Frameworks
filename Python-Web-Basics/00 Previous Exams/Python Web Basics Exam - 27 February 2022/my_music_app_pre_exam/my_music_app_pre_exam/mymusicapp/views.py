from django.shortcuts import render, redirect

from my_music_app_pre_exam.mymusicapp.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, \
    DeleteProfileForm
from my_music_app_pre_exam.mymusicapp.models import Profile, Album


# Create your views here.

def get_person():
    try:
        profile = Profile.objects.get()
        return profile
    except Profile.DoesNotExist:
        return None


def index(request):
    if get_person():
        data = {
            'albums': Album.objects.all(),

        }
        return render(request, 'core/home-with-profile.html', data)
    else:
        if request.method == 'GET':
            form = CreateProfileForm()
        else:
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')

        data = {
            'form': form,
            "no_user": True,
        }

        return render(request, 'core/home-no-profile.html', data)


def add_album(request):
    if request.method == 'GET':
        form = CreateAlbumForm()
    else:
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    data = {
        'form': form
    }

    return render(request, 'albums/add-album.html', data)


def album_details(request, pk):
    album = Album.objects.filter(pk=pk).get()

    data = {
        'album': album
    }

    return render(request, 'albums/album-details.html', data)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    data = {
        'album': album,
        'form': form,
    }

    return render(request, 'albums/edit-album.html', data)


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteAlbumForm(instance=album)
    else:
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    data = {
        'form': form,
        'album': album,
    }

    return render(request, 'albums/delete-album.html', data)


def profile_details(request):
    profile = get_person()
    albums = Album.objects.count()

    data = {
        'profile': profile,
        'albums': albums,
    }

    return render(request, 'profiles/profile-details.html', data)


def delete_profile(request):
    profile = get_person()
    print('predi requesta')
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
        print(form)
        print('test 2')
    else:
        print('test 1')
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            print('stana')
            form.save()
            return redirect('index')

    data = {
        'form': form,
    }

    return render(request, 'profiles/profile-delete.html', data)
