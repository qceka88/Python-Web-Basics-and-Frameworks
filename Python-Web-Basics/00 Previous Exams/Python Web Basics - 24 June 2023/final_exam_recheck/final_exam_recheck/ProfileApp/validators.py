from django.core import exceptions


def validate_profile_name_first_letter(value: str):
    if not value[0].isalpha():
        raise exceptions.ValidationError("Your name must start with a letter!")
