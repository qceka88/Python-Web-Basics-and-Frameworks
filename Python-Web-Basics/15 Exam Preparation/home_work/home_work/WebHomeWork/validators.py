from django.core import exceptions


def validate_username_characters(value: str):
    for character in value:
        if not character.isalnum() and character != '_':
            raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")
