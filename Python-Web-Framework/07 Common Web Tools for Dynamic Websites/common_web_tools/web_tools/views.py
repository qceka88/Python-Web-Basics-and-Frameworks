import random

from django.contrib.auth import get_user_model
from django import forms
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.views.decorators.cache import cache_page

from common_web_tools_lab.web_tools.models import Task
from django.views import generic as views

UserModel = get_user_model()


def before_request(request, *args, **kwargs):
    ...


def after_request(request, *args, **kwargs):
    ...


# Create your views here.
@cache_page(timeout=1)
def index(request):
    request.session['count'] = request.session.get('count', 0) + 1

    if not cache.get('users'):
        cache.set('users', UserModel.objects.all(), 1)

    users = cache.get('users')
    prev_tasks_ids = request.session.get('prev_tasks', [])
    context = {
        # 'count': random.randint(1, 10000),
        'count': request.session['count'],
        'users': users,
        'tasks': Task.objects.all(),
        'prev_tasks': Task.objects.filter(pk__in=prev_tasks_ids),

    }
    return render(request, 'index.html', context)


def details_task(request, pk):
    task = Task.objects.filter(pk=pk).get()
    prev_tasks = request.session.get('prev_tasks', [])
    prev_tasks.append(task.pk)

    start_index = max(0, len(prev_tasks) - 3)
    request.session.set_expiry(5 * 60)
    request.session['prev_tasks'] = prev_tasks[start_index:]

    return redirect('index')


def create_task(request):
    Task.objects.create(title=f"Title {random.randint(1, 10000)}")
    return redirect('index')


class TaskForm(forms.ModelForm):
    ...


class TaskCreate(views.CreateView):
    model = Task
    template_name = 'index.html'
