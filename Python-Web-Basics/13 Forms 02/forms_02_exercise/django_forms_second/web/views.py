from django.shortcuts import render

from django_forms_second.web.forms import TodoForm, TodoModelForm, ImageModelForm
from django_forms_second.web.models import ImageModel


# Create your views here.

def index(request):
    form_type = TodoModelForm
    form = form_type()

    if request.method == 'POST':
        form = form_type(request.POST)
        if form.is_valid():
            print(form.changed_data)

    context = {
        'form': form,
    }

    return render(request, 'web/index.html', context)


def create_image_view(request):
    form_type = ImageModelForm
    form = form_type()

    if request.method == 'POST':
        form = form_type(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.save()

    context = {
        'form': form,
        'images': ImageModel.objects.all(),
    }

    return render(request, 'web/create_image.html', context)
