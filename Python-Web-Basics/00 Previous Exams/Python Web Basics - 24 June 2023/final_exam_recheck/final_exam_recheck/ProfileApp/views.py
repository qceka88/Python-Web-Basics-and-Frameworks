from django.shortcuts import render, redirect

from final_exam_recheck.MainApp.views import find_profile
from final_exam_recheck.ProfileApp.forms import CreatePofileForm, EditPofileForm, DeletePofileForm
from final_exam_recheck.FruitApp.models import FruitModel


# Create your views here.
def profile_create(request):
    form = CreatePofileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard page')
    data = {
        'form': form,
        'not_registered_user': True,
    }
    return render(request, 'profiles/create-profile.html', data)


def profile_details(request):
    profile = find_profile()
    fruits = FruitModel.objects.all().count()

    data = {
        'profile': profile,
        'posts_number': fruits
    }
    return render(request, 'profiles/details-profile.html', data)


def profile_edit(request):
    profile = find_profile()
    form = EditPofileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile details')

    data = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/edit-profile.html', data)


def profile_delete(request):
    profile = find_profile()
    form = DeletePofileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        FruitModel.objects.all().delete()
        return redirect('home page')

    data = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/delete-profile.html', data)
