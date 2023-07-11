from django import forms
from django.core import validators, exceptions

from django_forms_second.web.models import TodoModel, ImageModel
from django_forms_second.web.validators import min_value_validator, max_value_validator, ValueInRangeValidator


class TodoForm(forms.Form):
    text = forms.CharField(
        validators=[
            validators.MinLengthValidator(5),
            validators.MaxLengthValidator(130),
        ],
        error_messages={
            'required': 'Please enter a todo item!!!!!! ',
            'min_length': 'Todo item must be at least 5 characters long!!!!!!!!!!!',
        }
    )

    done = forms.BooleanField(required=False)

    priority2 = forms.IntegerField(
        validators=[
            min_value_validator,
            max_value_validator,
        ],
    )

    priority = forms.IntegerField(
        validators=[
            ValueInRangeValidator(6, 10),
        ],
    )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     cleaned_data['text'] = cleaned_data['text'].upper()
    #
    # def clean_done(self):
    #     return self.cleaned_data['text']
    #
    # def clean_text(self):
    #     text = self.cleaned_data["text"]
    #
    #     if "bad" in text.lower():
    #         raise exceptions.ValidationError("Bad word detected")
    #
    #     return text.upper()


class TodoModelForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = '__all__'
        error_messages = {
            "text": {
                "required": "Please enter a todo item???? Pretty please????",
                "min_length": "Todo item must be at least 5 characters long!!!!!",

            }
        }


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'
