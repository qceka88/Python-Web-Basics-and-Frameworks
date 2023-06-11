from django.shortcuts import render, redirect

from car_collection_app_exam.car_collection.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, \
    EditProfileForm, DeleteProfileForm
from car_collection_app_exam.car_collection.models import Profile, Car


# Create your views here.
def index(request):
    data = {
        'profile': find_profile()
    }

    return render(request, 'core/index.html', data)


def profile_create(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    data = {
        'form': form,
        'profile': find_profile(),
    }

    return render(request, 'profiles/profile-create.html', data)


def catalogue_page(request):
    cars_list = Car.objects.all()

    data = {
        'cars': cars_list,
        'profile': find_profile(),
    }

    return render(request, 'cars/catalogue.html', data)


def car_create(request):
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    data = {
        'form': form,
        'profile': find_profile(),
    }

    return render(request, 'cars/car-create.html', data)


def car_details(request, pk):
    car_data = Car.objects.get(pk=pk)

    data = {
        'car_data': car_data,
        'profile': find_profile(),
    }

    return render(request, 'cars/car-details.html', data)


def car_edit(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    data = {
        'form': form,
        'car': car,
        'profile': find_profile(),
    }

    return render(request, 'cars/car-edit.html', data)


def car_delete(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    data = {
        'form': form,
        'car': car,
        'profile': find_profile(),
    }

    return render(request, 'cars/car-delete.html', data)


def profile_details(request):
    profile = find_profile().get()
    cars_total_price = sum([c.price for c in Car.objects.all()])
    profile_names = ' '.join(n for n in [profile.first_name, profile.last_name] if n)

    data = {
        'profile': profile,
        'total_price': cars_total_price,
        'profile_name': profile_names,
    }

    return render(request, 'profiles/profile-details.html', data)


def profile_edit(request):
    profile = find_profile().get()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details page')

    data = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/profile-edit.html', data)


def profile_delete(request):
    profile = find_profile().get()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index page')

    data = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/profile-delete.html', data)


# HELPING FUNCTIONS
def find_profile():
    try:
        return Profile.objects.all()

    except Profile.DoesNotExist:
        return None
