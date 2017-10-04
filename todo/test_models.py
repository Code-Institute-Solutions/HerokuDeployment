from django.test import TestCase
from .models import Item

# Create your tests here.
class TestItemModel(TestCase):
    def test_can_create_an_item_with_just_a_name(self):
        item = Item(name="any name");
        item.save();
        self.assertEqual(item.name, "any name")
        self.assertFalse(item.done)

    def test_can_create_an_item_with_name_and_status(self):
        item = Item(name="any name", done=True);
        item.save();
        self.assertEqual(item.name, "any name")
        self.assertTrue(item.done)
        
    def test_item_as_string(self):
        item = Item(name="An Item", done=True)
        self.assertEqual("An Item", str(item))