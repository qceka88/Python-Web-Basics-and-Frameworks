from django.core.exceptions import ValidationError

INVALID_PHONE_MESSAGE = 'Phone must start with "0" or "+"'


def validate_phone(value):
    if not value:
        raise ValidationError('Phone cannot be None')

    if not value.startswith('0') and not value.startswith('+'):
        raise ValidationError(INVALID_PHONE_MESSAGE)
