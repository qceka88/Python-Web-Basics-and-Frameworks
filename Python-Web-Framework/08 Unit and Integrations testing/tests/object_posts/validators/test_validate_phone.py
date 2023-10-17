from django.core.exceptions import ValidationError
from django.test import TestCase

from lost_and_found.objects_posts.vallidators import validate_phone, INVALID_PHONE_MESSAGE


class ValidatePhoneTests(TestCase):
    def test_validate_phone__when_starts_with_plus__expect_nothing(self):
        phone = '+123456'

        validate_phone(phone)

    def test_validate_phone__when_starts_with_zero__expect_nothing(self):
        phone = '0123456'

        validate_phone(phone)

    def test_validate_phone__when_not_starts_with_zero_or_plus__expect_nothing(self):
        phone = '10123456'

        with self.assertRaises(ValidationError) as ex:
            validate_phone(phone)

        self.assertIsNotNone(ex.exception)
        self.assertEqual(INVALID_PHONE_MESSAGE, *ex.exception)
