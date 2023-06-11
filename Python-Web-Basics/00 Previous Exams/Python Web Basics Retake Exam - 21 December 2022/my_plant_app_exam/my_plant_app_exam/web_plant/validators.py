from django.core import exceptions


def upper_case_validator(value: str):
    if not value[0].isupper():
        raise exceptions.ValidationError("Your name must start with a capital letter!")


def only_letters_validator(value: str):
    if not value.isalpha():
        raise exceptions.ValidationError("Plant name should contain only letters!")
