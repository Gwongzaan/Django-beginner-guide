from django.test import TestCase
from django.shortcuts import resolve_url
from lists.models import List, Item

class NewItemTest(TestCase):

    def test_pass_correct_list_to_template(self):
        otehr_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.get(resolve_url('view_list', list_id=correct_list.id) )
        self.assertEqual(response.context.get('list'), correct_list)

    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(resolve_url('add_item', list_id=correct_list.id), 
                         data={"item_text": 'A new item for an existing list'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "A new item for an existing list")
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(resolve_url('add_item', list_id=correct_list.id),
                                    data={'item_text': "A new item for an existing list"})

        self.assertRedirects(response, resolve_url('view_list', list_id=correct_list.id))

