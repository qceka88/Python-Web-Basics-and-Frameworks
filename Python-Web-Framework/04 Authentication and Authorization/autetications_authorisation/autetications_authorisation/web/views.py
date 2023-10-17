import random
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# from django.views import generic as views

UserModel = get_user_model()


# Create your views here.


@login_required
def index(request):
    user = random.randint(1, 1000)

    # good practice
    # UserModel.objects.create_user(
    #     username=f'admin{user}',
    #     email=f'admin{user}@example.com',
    #     password='1234',
    # )
    # bad practice
    # UserModel.objects.create(
    #     username=f'admin{user}',
    #     email=f'admin{user}@example.com',
    #     password='1234',
    # )
    some_object = UserModel.objects.get(username=f'admin63')
    # some_object = User.objects.get(username='admin')
    context = {
        "user": some_object,
        'permission': request.user.has_perm('web.view_user')
    }
    return render(request, 'index.html', context)


def login_user(request):
    user = authenticate(
        username='admin327',
        password='1234',
    )
    login(request, user)
    print(f"test result -->{user}")

    return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('index')
