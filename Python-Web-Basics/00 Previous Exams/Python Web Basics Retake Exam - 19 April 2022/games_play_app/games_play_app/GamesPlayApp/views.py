from django.shortcuts import render, redirect

from games_play_app.GamesPlayApp.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateGameForm, \
    EditGameForm, DeleteGameForm
from games_play_app.GamesPlayApp.models import Profile, GameModel


# Create your views here.
def index(request):
    data = {
        'profile': find_profile(),
    }

    return render(request, 'core/home-page.html', data)


def profile_create(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    data = {
        'form': form,
        'profile': find_profile()
    }

    return render(request, 'profiles/create-profile.html', data)


def dashboard_view(request):
    games_list = GameModel.objects.all()

    data = {
        'games': games_list,
        'profile': find_profile(),
    }

    return render(request, 'core/dashboard.html', data)


def game_create(request):
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    data = {
        'form': form,
        'profile': find_profile(),
    }

    return render(request, 'games/create-game.html', data)


def game_details(request, pk):
    game = GameModel.objects.get(pk=pk)

    data = {
        'game': game,
        'profile': find_profile(),
    }

    return render(request, 'games/details-game.html', data)


def game_edit(request, pk):
    game = GameModel.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    data = {
        'form': form,
        'game': game,
        'profile': find_profile(),
    }

    return render(request, 'games/edit-game.html', data)


def game_delete(request, pk):
    game = GameModel.objects.get(pk=pk)

    if request.method == 'GET':
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        game.delete()
        return redirect('dashboard page')

    data = {
        'form': form,
        'profile': find_profile(),
        'game': game,
    }

    return render(request, 'games/delete-game.html', data)


def profile_details(request):
    profile = find_profile().get()
    names = ' '.join(n for n in [profile.first_name, profile.last_name] if n)
    games = GameModel.objects.all().count()

    if games:
        average_rating = sum(g.rating for g in GameModel.objects.all()) / games
    else:
        average_rating = 0

    data = {
        'profile': profile,
        'names': names,
        'games_qty': games,
        'rating_average': average_rating,
    }

    return render(request, 'profiles/details-profile.html', data)


def profile_edit(request):
    profile = find_profile().get()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    data = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/edit-profile.html', data)


def profile_delete(request):
    profile = find_profile().get()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    data = {
        'form': form,
        'profile': profile,

    }

    return render(request, 'profiles/delete-profile.html', data)


# helping functions

def find_profile():
    try:
        return Profile.objects.all()
    except Profile.DoesNotExist:
        return None
