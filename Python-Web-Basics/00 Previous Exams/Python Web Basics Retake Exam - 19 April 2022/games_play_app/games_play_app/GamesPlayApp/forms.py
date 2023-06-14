from django import forms
from django.contrib.auth.hashers import make_password, check_password

from games_play_app.GamesPlayApp.models import Profile, GameModel


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']


class CreateProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class EditProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.TextInput(
                attrs={'type': 'password'}
            ),
        }


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            GameModel.objects.all().delete()
            self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()


class BaseGameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'
        labels = {
            'max_level': 'Max Level',
            'image_url': 'Image URL'
        }


class CreateGameForm(BaseGameForm):
    ...


class EditGameForm(BaseGameForm):
    ...


class DeleteGameForm(BaseGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_fields_inactive()

    # def save(self, commit=True):
    #     if commit:
    #         self.instance.delete()
    #
    #     return self.instance

    def __set_fields_inactive(self):
        for _, field in self.fields.items():
            # field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
