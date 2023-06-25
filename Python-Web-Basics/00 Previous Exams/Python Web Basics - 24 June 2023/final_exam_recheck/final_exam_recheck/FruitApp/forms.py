from django import forms

from final_exam_recheck.FruitApp.models import FruitModel


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }
        labels = {'image_url': 'Image URL'}


class CreateFruitForm(BaseFruitForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        widgets = BaseFruitForm.Meta.widgets
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }


class EditFruitForm(BaseFruitForm):
    ...


class DeleteFruitForm(BaseFruitForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_fields_disabled()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_fields_disabled(self):
        for field in self.fields.values():
            field.disabled = True

    class Meta:
        model = FruitModel
        exclude = ['nutrition']
        labels = BaseFruitForm.Meta.labels
