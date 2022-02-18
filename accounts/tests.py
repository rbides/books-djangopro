from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='Will',
            email='will@email.com',
            password='testpass123',
        )

        self.assertEqual(user.username, 'Will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='super',
            email='super@email.com',
            password='testpass123',
        )

        self.assertEqual(user.username, 'super')
        self.assertEqual(user.email, 'super@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupPageTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up') # tests the sign up button's text
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)