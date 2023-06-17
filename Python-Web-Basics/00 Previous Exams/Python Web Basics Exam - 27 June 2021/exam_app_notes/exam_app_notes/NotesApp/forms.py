from django import forms
from .models import Profile, Note


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Link to Profile Image',
        }


class CreateProfileForm(BaseProfileForm):
    ...


# class DeleteProfile(BaseProfileForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def save(self, commit=True):
#         if commit:
#             Note.objects.all().delete()
#             self.instance.delete()
#
#         return self.instance


class BaseNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'image_url']
        labels = {
            'image_url': 'Link To Image'
        }


class CreateNoteForm(BaseNoteForm):
    ...


class EditNoteForm(BaseNoteForm):
    ...


class DeleteNoteForm(BaseNoteForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
