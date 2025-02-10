from django.test import TestCase
from django.shortcuts import resolve_url
from lists.models import Item, List

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get(resolve_url('list', id=list_.id))
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_dislay_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text='item 1', list=list_)
        Item.objects.create(text='item 2', list=list_)

        response = self.client.get(resolve_url('home'))
        self.assertIn('item 1', response.content.decode())
        self.assertIn('item 2', response.content.decode())

    def test_display_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text="item1", list=correct_list)
        Item.objects.create(text='item2', list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(text='other list item 1', list=other_list)
        Item.objects.create(text="other list item2", list=other_list)

        response = self.client.get(resolve_url('list', id=correct_list.id))

        self.assertContains(response, "item 1")
        self.assertContains(response, 'item 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item2')
