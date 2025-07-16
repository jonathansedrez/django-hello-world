from django.test import TestCase
from django.urls import reverse

class IndexViewTests(TestCase):
    def test_index_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_template_used(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, "todos/index.html")

    def test_index_contains_message(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, "Insert new to-do")
