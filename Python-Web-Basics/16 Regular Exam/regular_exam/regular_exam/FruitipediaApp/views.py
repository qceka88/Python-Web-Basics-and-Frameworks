from django.shortcuts import render, redirect
from .models import ProfileModel, FruitModel
from .forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateFruitForm, EditFruitForm, \
    DeleteFruitForm


# Create your views here.
def index(request):
    data = {
        'not_registered_user': False if find_profile() else True,
    }
    return render(request, 'core/index.html', data)


def dashboard_page(request):
    if not find_profile():
        return redirect('index page')

    fruits = FruitModel.objects.all().order_by('pk')

    data = {
        'fruit_list': fruits,
    }

    return render(request, 'core/dashboard.html', data)


def fruit_create_page(request):
    if not find_profile():
        return redirect('index page')

    form = CreateFruitForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard page')

    data = {
        'form': form,
    }

    return render(request, 'fruits/create-fruit.html', data)


def fruit_details_page(request, fruitID):
    if not find_profile():
        return redirect('index page')

    fruit = find_fruit(fruitID)
    data = {
        'fruit': fruit,
    }
    return render(request, 'fruits/details-fruit.html', data)


def fruit_edit_page(request, fruitID):
    if not find_profile():
        return redirect('index page')

    fruit = FruitModel.objects.filter(pk=fruitID).get()
    form = EditFruitForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard page')

    data = {
        'fruit': fruit,
        'form': form,
    }
    return render(request, 'fruits/edit-fruit.html', data)


def fruit_delete_page(request, fruitID):
    fruit = FruitModel.objects.filter(pk=fruitID).get()
    form = DeleteFruitForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard page')

    data = {'fruit': fruit,
            'form': form,
            }

    return render(request, 'fruits/delete-fruit.html', data)


def profile_create_page(request):
    if find_profile():
        return redirect('index page')

    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard page')

    data = {
        'form': form,
        'not_registered_user': True,
    }
    return render(request, 'profiles/create-profile.html', data)


def profile_details_page(request):
    if not find_profile():
        return redirect('index page')

    profile = find_profile()
    fruits_number = FruitModel.objects.all().count()
    data = {
        'profile': profile,
        'posts': fruits_number,
    }
    return render(request, 'profiles/details-profile.html', data)


def profile_edit_page(request):
    if not find_profile():
        return redirect('index page')

    profile = find_profile()
    form = EditProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile details page')

    data = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/edit-profile.html', data)


def profile_delete_page(request):
    if not find_profile():
        return redirect('index page')
    profile = find_profile()
    form = DeleteProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('index page')
    data = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/delete-profile.html', data)


# helping functions
def find_profile():
    try:
        return ProfileModel.objects.all().first()
    except ProfileModel.DoesNotExist:
        return None


def find_fruit(id_num):
    return FruitModel.objects.filter(pk=id_num).get()
