from django.test import TestCase
from . import setup_data
from django.urls import reverse 
from users.models import UserProfile

class TestBookAPIView(TestCase):
    def setUp(self):
        self.users = setup_data.create_users()
        self.books = setup_data.create_book_data()
        self.uri = reverse("api_books:books")

    def test_get_request(self):
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200) 
        self.assertEqual('"unauthorized"', response.content.decode(encoding='utf-8'))

    def test_get_request_with_parameters(self):
        response = self.client.get(self.uri, {"apikey": self.users.get('user1').APIkey, 'isbn':self.books.get('book1').isbn })
        # in practicle, it is usually use MOdelSerializer
        balance = UserProfile.objects.get(APIkey=self.users.get('user1').APIkey).balance
        self.assertEqual(self.users.get('user1').balance - 1, balance)

class TestMixinBookAPIView(TestCase):
    def setUp(self):
        self.users = setup_data.create_users()
        self.books = setup_data.create_book_data()
        self.uri = reverse('api_books:books3')

    def test_get_request_with_params(self):
        response = self.client.get(self.uri, {'apikey': self.users.get('user2').APIkey, 'isbn': self.books.get('book3').isbn})
        print(response.status_code)
        print(response.content)

class TestBookModelViewSEts(TestCase):
    def setUp(self):
        self.users = setup_data.create_users()
        self.books = setup_data.create_book_data()
        self.uri = reverse('api_books:api-list') 

    def test_get_request_with_params(self):
        response = self.client.get(self.uri, {'apikey': self.users.get('user2').APIkey, 'isbn': self.books.get('book3').isbn})
        print(response.status_code)
        print(response.content)