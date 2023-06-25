from django import forms
from .models import ProfileModel, FruitModel


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    class Meta:
        model = ProfileModel
        exclude = ['image_url', 'age']
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password'
                }
            ),
        }


class EditProfileForm(BaseProfileForm):
    class Meta:
        model = ProfileModel
        exclude = ['password', 'email']
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name',
            'image_url': 'Image URL:',
        }


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            FruitModel.objects.all().delete()
            self.instance.delete()
        return self.instance

    class Meta:
        model = ProfileModel
        fields = ()


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'


class CreateFruitForm(BaseFruitForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Fruit Name'}
            ),
            'image_url': forms.TextInput(
                attrs={'placeholder': 'Fruit Image URL'}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Fruit Description'}
            ),
            'nutrition': forms.Textarea(
                attrs={'placeholder': 'Nutrition info'}
            ),
        }


class EditFruitForm(BaseFruitForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        labels = {

            'image_url': 'Image URL:',

        }
        widgets = {
            'nutrition': forms.Textarea(
                attrs={'placeholder': 'Nutrition info'}
            ),
        }


class DeleteFruitForm(BaseFruitForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.disabled = True

    class Meta:
        model = FruitModel
        exclude = ['nutrition']
        labels = {
            'image_url': 'Image URL:',
        }
