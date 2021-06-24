from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snacks

class SnacksTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester",
            email="test@email.com",
            password="password1234"
        )
        self.snacks = Snacks.objects.create(
            name="pickle",
            purchaser= self.user,
            description="nice"
        )
    def test_home_page_200(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_200(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_faq_page_200(self):
        url = reverse('faq')
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

    def test_faq_page_template_used(self):
        url = reverse('faq')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "faq.html")
        self.assertTemplateUsed(response, "base.html")

    def test_snack_list_view(self):
        response = self.client.get(reverse("snacks_list"))
        self.assertContains(response, "pickle")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snacks_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser:tester")
        self.assertTemplateUsed((response, "snacks_detail.html"))

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snacks_create"),
            {
                "name": "Ice Cream",
                "purchaser": self.user.id,
                "description": "yum",
            }, follow=True
        )

        self.assertRedirects(response, reverse("snacks_detail",
        args="2"))
        self.assertContains(response, "Description:yum")