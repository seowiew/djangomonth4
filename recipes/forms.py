from django import forms
from .models import Recipe, Ingredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description']
        labels = {
            'title': 'Название рецепта',
            'description': 'Описание рецепта',
        }

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'recipe']
        labels = {
            'name': 'Название ингредиента',
            'quantity': 'Количество',
            'recipe': 'Рецепт',
        }
