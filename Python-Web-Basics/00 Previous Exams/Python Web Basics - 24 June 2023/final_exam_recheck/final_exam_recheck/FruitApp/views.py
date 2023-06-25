from django.shortcuts import render, redirect

from final_exam_recheck.FruitApp.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
from final_exam_recheck.FruitApp.models import FruitModel


# Create your views here.
def fruit_create(request):
    form = CreateFruitForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard page')

    data = {
        'form': form,
    }
    return render(request, 'fruits/create-fruit.html', data)


def fruit_details(request, fruitID):
    fruit = find_fruit(fruitID)
    data = {
        'fruit': fruit,
    }
    return render(request, 'fruits/details-fruit.html', data)


def fruit_edit(request, fruitID):
    fruit = find_fruit(fruitID)
    form = EditFruitForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard page')

    data = {
        'fruit': fruit,
        'form': form,
    }
    return render(request, 'fruits/edit-fruit.html', data)


def fruit_delete(request, fruitID):
    fruit = find_fruit(fruitID)
    form = DeleteFruitForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard page')

    data = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruits/delete-fruit.html', data)


# helping functions
def find_fruit(id_num):
    return FruitModel.objects.filter(pk=id_num).get()
