from django.shortcuts import render, redirect
from home_work.WebHomeWork.models import ProfileModel, AlbumModel
from home_work.WebHomeWork.forms import CreateProfileForm, DeleteProfileForm, CreateAlbumForm, EditAlbumForm, \
    DeleteAlbumForm


# Create your views here.
def index(request):
    if not find_profile():
        return add_profile(request)
    else:
        albums_list = AlbumModel.objects.all().order_by('pk')

        context = {
            'albums_list': albums_list,
        }

        return render(request, 'core/home-with-profile.html', context)


def album_add_page(request):
    if not find_profile():
        return add_profile(request)

    form = CreateAlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'albums/add-album.html', context)


def details_album_page(request, id):
    if not find_profile():
        return add_profile(request)
    album = find_album(id)

    context = {
        'album': album
    }
    return render(request, 'albums/album-details.html', context)


def edit_album_page(request, id):
    if not find_profile():
        return add_profile(request)
    album = find_album(id)
    form = EditAlbumForm(request.POST or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect('home page')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'albums/edit-album.html', context)


def delete_album_page(request, id):
    if not find_profile():
        return add_profile(request)

    album = find_album(id)
    form = DeleteAlbumForm(request.POST or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect('home page')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'albums/delete-album.html', context)


def add_profile(request):
    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home page')

    context = {
        'form': form,
        'not_registered_user': True,
    }

    return render(request, 'core/home-no-profile.html', context)


def profile_details_page(request):
    profile = find_profile()
    if not profile:
        return add_profile(request)

    context = {
        'profile': profile,
        'albums_count': AlbumModel.objects.all().count(),
    }

    return render(request, 'profiles/profile-details.html', context)


def profile_delete_page(request):
    profile = find_profile()
    if not profile:
        return add_profile(request)

    form = DeleteProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('home page')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/profile-delete.html', context)


# helping functions
def find_profile():
    try:
        return ProfileModel.objects.all().first()
    except ProfileModel.DoesNotExist:
        return None


def find_album(id_num):
    return AlbumModel.objects.get(id=id_num)
