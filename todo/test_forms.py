from django.test import TestCase
from django import forms
from .forms import ItemForm

# Create your tests here.
class TestToDoItemForm(TestCase):
    def test_can_create_an_item_with_just_a_name(self):
        form = ItemForm({'name': "Create Tests"});
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_name(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['name'], [u'This field is required.'])
