from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipes:recipe_list')

class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes:recipe_list')
    template_name = 'recipes/recipe_confirm_delete.html'

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'recipes/ingredient_form.html'

    def get_success_url(self):
        return reverse_lazy('recipes:recipe_detail', kwargs={'pk': self.object.recipe.pk})

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs['pk']
        return super().form_valid(form)
