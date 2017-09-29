from django.test import TestCase
from .models import Item
from django.shortcuts import get_object_or_404

class TestViews(TestCase):
    def test_home_page_lists_todo_items(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "todo_list.html")


    def test_get_add_item_page(self):
        page = self.client.get('/add')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")


    def test_get_edit_item_page(self):
        item = Item(name='An Item')
        item.save()
        page = self.client.get('/edit/{0}'.format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")


    def test_get_edit_item_that_does_not_exist(self):
        page = self.client.get('/edit/1')
        self.assertEqual(page.status_code, 404)
        
        
    def test_post_create_item(self):
        response = self.client.post('/add', {'name': 'A Name'})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)
        
        
    def test_post_edit_item(self):
        item = Item(name='a name', done=True)
        item.save()
        id = item.id

        response = self.client.post('/edit/{0}'.format(id), {'name': 'A Different Name', 'done': False})

        item = get_object_or_404(Item, pk=id)

        self.assertEqual(item.name, 'A Different Name')
        self.assertEqual(item.done, False)

    def test_toggle_item(self):
        item = Item(name='An Item')
        item.save()
        response = self.client.post('/toggle/{0}'.format(item.id))

        item = get_object_or_404(Item, pk=item.id)
        self.assertEqual(item.done, True)
        
        self.assertEqual(response.status_code, 302)


