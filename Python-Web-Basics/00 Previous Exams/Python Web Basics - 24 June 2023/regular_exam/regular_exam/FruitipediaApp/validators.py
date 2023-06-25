from django.core import exceptions


def validate_profile_name_first_letter(value: str):
    if not value[0].isalpha():
        raise exceptions.ValidationError("Your name must start with a letter!")

def validate_fruit_name(value:str):
    for char in value:
        if not char.isalpha():
            raise exceptions.ValidationError("Fruit name should contain only letters!")