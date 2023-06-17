from django.shortcuts import render, redirect
from exam_recipes.Recipes.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm

from exam_recipes.Recipes.models import Recipe


# Create your views here.
def index(request):
    recipes = Recipe.objects.all()

    data = {
        'recipes_list': recipes
    }

    return render(request, 'core/index.html', data)


def create_recipe(request):
    form = CreateRecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home page')

    data = {
        'form': form,

    }
    return render(request, 'recipes/create.html', data)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = EditRecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('home page')

    data = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'recipes/edit.html', data)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        form = DeleteRecipeForm(instance=recipe)
    else:
        recipe.delete()
        return redirect('home page')

    data = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'recipes/delete.html', data)


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')
    data = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'recipes/details.html', data)
