from django.test import TestCase
from django.urls import reverse
from .models import Todo 

class TodoViewTests(TestCase):
    def setUp(self): # called before each individual test method
        Todo.objects.create(todo_label="Learn Django", is_checked=False)
        Todo.objects.create(todo_label="Build a test", is_checked=True)

    def test_template_used(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'todos/index.html')

    def test_todo_list_todos(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, "Learn Django")
        self.assertContains(response, "Build a test")
        self.assertContains(response, '<fieldset>', count=3) # input + todos created on setUp

    def test_add_todo(self):
        response = self.client.post(reverse('index'), {'new-todo': 'Write unit tests'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Todo.objects.filter(todo_label='Write unit tests').exists())