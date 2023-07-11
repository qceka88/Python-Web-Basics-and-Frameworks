from django.core import exceptions
from django.utils.deconstruct import deconstructible


def min_value_validator(value):
    if value < 1:
        raise exceptions.ValidationError('Value cannot be negative')


def max_value_validator(value):
    if value > 10:
        raise exceptions.ValidationError('Value cannot be greater than 10')


@deconstructible
class ValueInRangeValidator:

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if value < self.min_value:
            raise exceptions.ValidationError(f'MCV: Value cannot be less than {self.min_value}', code='min_value')
        if value > self.max_value:
            raise exceptions.ValidationError(f'MCV: Value cannot be greater than {self.max_value}', code='max_value')

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (
                self.limit_value == other.limit_value
                and self.min_value == other.min_value
                and self.min_value == other.max_value
        )
