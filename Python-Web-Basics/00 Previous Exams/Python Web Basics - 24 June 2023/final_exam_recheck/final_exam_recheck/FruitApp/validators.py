from django.core import exceptions


def validate_fruit_name(value: str):
    for char in value:
        if not char.isalpha():
            raise exceptions.ValidationError("Fruit name should contain only letters!")
