from django import forms

from exam_recipes.Recipes.models import Recipe


class BaseRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
            'recipe_time': 'Time(Minutes)',
        }


class CreateRecipeForm(BaseRecipeForm):
    ...


class EditRecipeForm(BaseRecipeForm):
    ...


class DeleteRecipeForm(BaseRecipeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_fields_disabled()

    def __set_fields_disabled(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
