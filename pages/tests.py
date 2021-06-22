from django.test import SimpleTestCase
from django.urls import reverse

class PagesTest(SimpleTestCase):
    def test_home_page_200(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_200(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "home.html")
        self.assertTemplateUsed(response, "base.html")

    def test_about_page_template_used(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "about.html")
        self.assertTemplateUsed(response, "base.html")
