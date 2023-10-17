from django.core import exceptions


def validate_value_between_0_and_1(value):
    if value < 0 or value > 1:
        raise exceptions.ValidationError('>>><<<<<')
