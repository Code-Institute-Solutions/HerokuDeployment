from django.apps import apps
from django.test import TestCase
from .apps import TodoConfig


class TodoConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(TodoConfig.name, 'todo')
        self.assertEqual(apps.get_app_config('todo').name, 'todo')