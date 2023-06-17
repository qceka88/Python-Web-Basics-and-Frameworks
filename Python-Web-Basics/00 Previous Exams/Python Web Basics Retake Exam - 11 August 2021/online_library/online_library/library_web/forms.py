from django import forms

from online_library.library_web.models import Profile, Book


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL'
        }


class CreateProfileForm(BaseProfileForm):
    ...


class EditProfileForm(BaseProfileForm):
    ...


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'


class BaseBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description'
                }
            ),
            'image': forms.TextInput(
                attrs={
                    'placeholder': 'Image'
                }
            ),
            'book_type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime..'
                }
            ),
        }


class CreateBookForm(BaseBookForm):
    ...


class EditBookForm(BaseBookForm):
    ...
