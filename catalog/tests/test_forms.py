from django.test import TestCase

from catalog.forms import AuthorCreationForm


class FormTest(TestCase):

    def test_author_creation_with_pseudonym_last_name_first_name(self):
        form_data = {
            "username": "username",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "First test",
            "last_name": "Last test",
            "pseudonym": "test Pseudonym"
        }
        form = AuthorCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
