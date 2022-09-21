from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import LiteraryFormat

LITERARY_FORMAT_URL = reverse("catalog:literary-format-list")


class PublicLiteraryFormatTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(LITERARY_FORMAT_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateLiteraryFormatTest(TestCase):

    def setUp(self) ->None:
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="test",
            password="user12345"
        )
        self.client.force_login(self.user)

    def test_retrieve_literary_formats(self):
        LiteraryFormat.objects.create(name="poetry")
        LiteraryFormat.objects.create(name="drama")

        resp = self.client.get(LITERARY_FORMAT_URL)
        literary_formats = LiteraryFormat.objects.all()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(list(resp.context["literary_format_list"]), list(literary_formats))
        self.assertTemplateUsed(resp, "catalog/literary_format_list.html")


class PrivateAuthorTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="user12345"
        )
        self.client.force_login(self.user)

    def test_create_author(self):
        form_data = {
            "username": "new_user",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "First test",
            "last_name": "Last test",
            "pseudonym": "test Pseudonym"
        }
        self.client.post(reverse("catalog:author-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.pseudonym, form_data["pseudonym"])
