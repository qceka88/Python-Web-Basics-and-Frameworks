from django import forms

from final_exam_recheck.ProfileApp.models import ProfileModel


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Image URL'})
        }


class CreatePofileForm(BaseProfileForm):
    class Meta:
        model = ProfileModel
        exclude = ['image_url', 'age']
        widgets = BaseProfileForm.Meta.widgets
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }


class EditPofileForm(BaseProfileForm):
    class Meta:
        model = ProfileModel
        exclude = ['password', 'email']
        widgets = BaseProfileForm.Meta.widgets

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }


class DeletePofileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    class Meta:
        model = ProfileModel
        fields = ()
