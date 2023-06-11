from django.shortcuts import render, redirect

from my_plant_app_exam.web_plant.forms import CreateProfileForm, EditProfileForm, CreatePlantForm, DeletePlantForm, \
    EditPlantForm, DeleteProfileForm
from my_plant_app_exam.web_plant.models import Profile, Plant


# Create your views here.

def index(request):
    data = {
        'profile': get_profile()
    }

    return render(request, 'core/home-page.html', data)


def profile_create_page(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    data = {
        'form': form,
    }

    return render(request, 'profiles/create-profile.html', data)


def catalogue(request):
    plants_queryset = Plant.objects.all()

    data = {
        'plants': plants_queryset,
        'profile': get_profile(),
    }

    return render(request, 'plants/catalogue.html', data)


def plant_create_page(request):
    if request.method == 'GET':
        form = CreatePlantForm()
    else:
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    data = {
        'form': form,
        'profile': get_profile(),
    }

    return render(request, 'plants/create-plant.html', data)


def plant_edit_page(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditPlantForm(instance=plant)
    else:
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    data = {
        'form': form,
        'plant': plant,
        'profile': get_profile(),
    }

    return render(request, 'plants/edit-plant.html', data)


def plant_details_page(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    data = {
        'plant': plant,
        'profile': get_profile(),
    }

    return render(request, 'plants/plant-details.html', data)


def plant_delete_page(request, pk):
    plant = Plant.objects.get(pk=pk)

    if request.method == 'GET':
        form = DeletePlantForm(instance=plant)
    else:
        form = DeletePlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    data = {
        'form': form,
        'plant': plant,
        'profile': get_profile(),
    }

    return render(request, 'plants/delete-plant.html', data)


def profile_details_page(request):
    profile = get_profile().get()
    plants = Plant.objects.all()[:3]
    data = {
        'profile': profile,
        'count_of_plants': plants,
    }

    return render(request, 'profiles/profile-details.html', data)


def profile_edit_page(request):
    profile = get_profile().get()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    data = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/edit-profile.html', data)


def profile_delete_page(request):
    profile = get_profile().get()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    data = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/delete-profile.html', data)


# helping functions

def get_profile():
    try:
        profile = Profile.objects.all()
        return profile

    except Profile.DoesNotExist:
        return None
