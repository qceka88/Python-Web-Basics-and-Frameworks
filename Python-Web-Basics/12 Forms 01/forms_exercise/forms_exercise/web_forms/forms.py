from django import forms

from django_forms.forms_web.models import Person


class PersonModelForm(forms.ModelForm):
    story = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control"
            }

        )
    )

    class Meta:
        model = Person
        fields = '__all__'
        exclude = ['password']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "name input"
                }
            ),
        }

        labels = {
            'name': "custom input blqh"
        }

        help_texts = {
            "age": "please fill your age"
        }


class PersonForm(forms.Form):
    name = forms.CharField(
        label='Your name',
        max_length=100,
        required=False,
        # widget=forms.Textarea(),
        widget=forms.TextInput(
            attrs={
                "placeholder": "YOur placehold name",
                "class": "form-control",
                "custom-attribute": "custom-value",
            }
        )
    )

    age = forms.IntegerField(
        initial=18,
        help_text='Please fill your age!',
    )

    # HOBBY_CHOICES = [
    #     (1, 'Football'),
    #     (2, 'Basketball'),
    #     (3, 'Tennis'),
    # ]
    #
    # hobby = forms.CharField(widget=forms.RadioSelect(
    #     choices=HOBBY_CHOICES))
    #
    # hobby3 = forms.CharField(widget=forms.Select(
    #     choices=HOBBY_CHOICES))
    #
    # is_happy = forms.BooleanField()

    # email = forms.EmailField()
    # password = forms.CharField()
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput,
    # )
    # url_input1 = forms.URLInput()
    #
    # url_input2 = forms.CharField(
    #     widget=forms.URLInput,
    # )
    #
    # date_input = forms.DateField()
    # date_input2 = forms.CharField(
    #     widget=forms.DateTimeInput,
    # )
    # date_input3 = forms.CharField(
    #     widget=forms.DateTimeInput,
    # )
