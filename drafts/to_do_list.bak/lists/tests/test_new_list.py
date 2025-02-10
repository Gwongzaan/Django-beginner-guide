from django.test import TestCase
from django.shortcuts import resolve_url

class newlistTest(TestCase):
    def test_can_save_a_POST_request(self):
        self.client.post(resolve_url('new_list'), data={'item_text': 'A new list item'})
        self.assertEqual(item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def rest_redirects_after_post(self):
        response = self.client.post(resolve_url('new_list'), data={'item_text': 'A new list item'})
        new_list = List.objects.first()
        self.assertRedirects(response, resolve_url('view_list', new_list.id))
