from django import forms

from home_work.WebHomeWork.models import ProfileModel, AlbumModel


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age'
                }
            ),
        }


class CreateProfileForm(BaseProfileForm):
    ...


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            AlbumModel.objects.all().delete()
            self.instance.delete()
        return self.instance

    class Meta:
        model = ProfileModel
        fields = ()


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'
        labels = {
            'album_name': 'Album Name:',
            'image_url': 'Image URL',
        }
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name'
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description'
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price'
                }
            ),
        }


class CreateAlbumForm(BaseAlbumForm):
    ...


class EditAlbumForm(BaseAlbumForm):
    ...


class DeleteAlbumForm(BaseAlbumForm):
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
