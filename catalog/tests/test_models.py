from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.models import LiteraryFormat, Book


class ModelTest(TestCase):

    def test_literary_format_str(self):
        format_ = LiteraryFormat.objects.create(name="test")

        self.assertEqual(str(format_), format_.name)

    def test_author_str(self):
        author = get_user_model().objects.create_user(
            username="test",
            first_name="First",
            last_name="Last",
            password="test1234"
        )

        self.assertEqual(str(author), f"{author.username} ({author.first_name} {author.last_name})")

    def test_Book_str(self):
        format_ = LiteraryFormat.objects.create(name="test")
        book = Book.objects.create(
            title="Test",
            price=10.15,
            format=format_
        )

        self.assertEqual(str(book), f"{book.title} (price: {book.price}, format: {book.format.name})")

    def test_author_pseudonym(self):
        username = "test"
        password = "test1234"
        pseudonym = "test_pseudo"

        author = get_user_model().objects.create_user(
            username="test",
            password="test1234",
            pseudonym=pseudonym
        )

        self.assertEqual(author.username, username)
        self.assertTrue(author.check_password(password))
        self.assertEqual(author.pseudonym, pseudonym)
