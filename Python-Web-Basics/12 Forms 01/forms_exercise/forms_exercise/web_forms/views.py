from django.shortcuts import render

from django_forms.forms_web.forms import PersonForm, PersonModelForm
from django_forms.forms_web.models import Person


# Create your views here.
def index(request):
    if request.method == 'GET':
        form = PersonForm()
        name = None

    else:
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            # can create model from cleaned data!!
            # Person.objects.create(**form.cleaned_data)
            Person.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
            )
            people = Person.objects.all()

    context = {
        'form': form,
        'name': name,
        'people': people,
    }

    return render(request, 'web_forms/index.html', context)


def model_form_view(request):
    # person = Person.objects.get(id=2)

    form = PersonModelForm()

    if request.method == 'POST':
        form = PersonModelForm(request.POST)
        if form.is_valid():
            story = form.cleaned_data["story"]
            if story == "I am happy":
                form.save()
                form = PersonModelForm()

    context = {
        'model_form': form,
    }

    return render(request, 'web_forms/model_form.html', context)
