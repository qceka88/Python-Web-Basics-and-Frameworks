from django import forms

from car_collection_app_exam.car_collection.models import Profile, Car


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class CreateProfileForm(BaseProfileForm):
    ...


class EditProfileForm(BaseProfileForm):


    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }


class DeleteProfileForm(BaseProfileForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'car_type': 'Type',
            'car_model': 'Model',
            'year': 'Year',
            'image_url': 'Image URL',
            'price': 'Price',
        }


class CreateCarForm(BaseCarForm):
    ...


class EditCarForm(BaseCarForm):
    ...


class DeleteCarForm(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_read_only_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_read_only_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
