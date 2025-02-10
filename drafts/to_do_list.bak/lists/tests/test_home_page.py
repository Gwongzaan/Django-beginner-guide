from django.test import TestCase
from django.shortcuts import resolve_url
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string

from lists.models import Item

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view_method_1(self):
        found = resolve(resolve_url('home'))
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8').strip()
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_home_page_returns_correct_html_method_3(self):
        response =  self.client.get('/')
        html = response.content.decode('utf8').strip()
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirect_after_POST(self):
        response = self.client.post(resolve_url('home'), data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.get('location'), '-list-in-the-world')

#        self.assertIn('A new list item', response.content.decode())
#        self.assertTemplateUsed(response, 'lists/home.html')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_dislay_all_items(self):
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        response = self.client.get(resolve_url('home'))
        self.assertIn('item 1', response.content.decode())
        self.assertIn('item 2', response.content.decode())
