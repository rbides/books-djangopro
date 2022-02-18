from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import AboutPageView, HomePageView


# SimpleTestCase is designed for webpages that do not have a model included
class HomePageTests(SimpleTestCase):
    
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_corret_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )

    def test_homepage_url_resolves_homepageview(self):
        # tests if the url resolves in the correct view
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):
    
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_homepage_contains_corret_html(self):
        self.assertContains(self.response, 'About Page')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )

    def test_homepage_url_resolves_homepageview(self):
        # tests if the url resolves in the correct view
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
