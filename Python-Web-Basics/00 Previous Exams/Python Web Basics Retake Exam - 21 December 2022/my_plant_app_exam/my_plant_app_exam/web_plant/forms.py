from django import forms

from my_plant_app_exam.web_plant.models import Profile, Plant


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']
        labels = {
            "username": "Username",
            "first_name": "First Name",
            "last_name": "Last Name",
        }


class CreateProfileForm(BaseProfileForm):
    ...


class EditProfileForm(BaseProfileForm):
    BaseProfileForm.Meta.fields += ['profile_picture']
    BaseProfileForm.Meta.labels.update({'profile_picture': 'Profile Picture'})


class DeleteProfileForm(BaseProfileForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def save(self, commit=True):
        if commit:
            Plant.objects.all().delete()
            self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()


class BasePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            "plant_type": "Type",
            "name": "Name",
            "image_url": "Image Url",
            "description": "Description",
            "price": "Price",
        }


class CreatePlantForm(BasePlantForm):
    ...


class EditPlantForm(BasePlantForm):
    ...


class DeletePlantForm(BasePlantForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
