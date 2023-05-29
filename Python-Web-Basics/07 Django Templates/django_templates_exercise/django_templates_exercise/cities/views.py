from django.http import HttpResponse
from django.shortcuts import render, redirect

from django_templates_exercise.cities.models import City


# Create your views here.
def all_cities(request):
    data = {
        f"{c.city_name.lower()}": c for c in City.objects.all()
    }

    return render(request, 'city_list.html', data)


def city_by_data(request, city_data):
    try:
        city_id = int(city_data)
        try:
            city = next(filter(lambda c: c.id == city_id, City.objects.all()))
        except StopIteration:
            return redirect('no such city')

    except ValueError:
        try:
            city = next(filter(lambda c: c.city_name == city_data, City.objects.all()))

        except StopIteration:
            return redirect('no such city')

    data = {
        'city': city,
    }
    return render(request, 'single_city.html', data)


def exercise(request):
    city_object = City.objects.all()

    data = {
        'city_list': city_object
    }

    return render(request, 'exercises.html', data)


def no_such_city(request):
    return render(request, 'city_404.html')
