from django.core import exceptions


def min_len_username_validations(value):
    if len(value) < 2:
        raise exceptions.ValidationError("The username must be a minimum of 2 chars")


def valid_year_check(value):
    min_year = 1980
    max_year = 2049
    if not min_year <= value <= max_year:
        raise exceptions.ValidationError("Year must be between 1980 and 2049")
