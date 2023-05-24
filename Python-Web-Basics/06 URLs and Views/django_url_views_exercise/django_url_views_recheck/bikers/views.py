from cgitb import html

from django.http import HttpResponse
from django.shortcuts import render, redirect

from django_url_views_recheck.bikers.models import Bikers


# Create your views here.

def empty(request):
    output = "<h1>Nothings here!</h1>"
    return HttpResponse(output)


def bikers(request):
    bikers_list = Bikers.objects.all()
    content = {'bikers_list': bikers_list}
    return render(request, 'html/index.html', content)


def bikers_id(request, some_id):
    try:
        biker = next(filter(lambda b: b.id == some_id, Bikers.objects.all()))
    except StopIteration:
        return redirect('non existing biker')

    return HttpResponse(f"<h1>{biker}</h1>")


def non_existing_biker(request):
    return HttpResponse('<h1 style="font-size: 150px">NO. Such biker!</h1>')
