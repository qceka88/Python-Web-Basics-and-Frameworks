from django.shortcuts import render

from django_project.students.models import Students


# Create your views here.
def home_view(request):
    students_list = Students.objects.all()
    context = {'students_list': students_list}
    return render(request, 'index.html', context)
