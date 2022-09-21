from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class TestAdmin(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345"
        )
        self.client.force_login(self.admin_user)

        self.author = get_user_model().objects.create_user(
            username="author",
            password="author12345",
            pseudonym="pseudonym"
        )

    def test_author_pseudonym_listed(self):
        url = reverse("admin:catalog_author_changelist")
        resp = self.client.get(url)

        self.assertContains(resp, self.author.pseudonym)

    def test_author_pseudonym_detail_listed(self):
        url = reverse("admin:catalog_author_change", args=[self.author.id])
        resp = self.client.get(url)

        self.assertContains(resp, self.author.pseudonym)
        
