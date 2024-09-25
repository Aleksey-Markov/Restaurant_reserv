from django.test import TestCase

from users.models import User


class UserTest(TestCase):

    def test_user_create(self):
        user = User('e@email.com', '8800', 'petya')
        self.assertEqual(user.name, 'petya')
        self.assertEqual(user.phone, '8800')
        self.assertEqual(user.email, 'e@email.com')

