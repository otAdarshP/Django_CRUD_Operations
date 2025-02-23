from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm

# Home page - List all recipes
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/index.html', {'recipes': recipes})

# Detail view of a recipe
def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})

# Create a new recipe
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'recipe/recipe_form.html', {'form': form})

# Edit an existing recipe
def recipe_edit(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe/recipe_form.html', {'form': form})

# Delete a recipe
def recipe_delete(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('index')
    return render(request, 'recipe/recipe_confirm_delete.html', {'recipe': recipe})

