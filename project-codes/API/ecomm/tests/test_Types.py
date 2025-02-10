from django.test import TestCase
from django.urls import reverse
from . import setup_data

class TestType1View(TestCase):
    def setUp(self):
        self.types = setup_data.create_types()
        self.uri = reverse('api_ecomm:type2')

    def test_Type1_get(self):
        response = self.client.get(self.uri)
        print(response.status_code)
        print(response.content)

class TestCategoryAPIView(TestCase):
    def setUp(self):
        self.types = setup_data.create_categories()


    def test_category_get(self):
        response = self.client.get(reverse('api_ecomm:category'))
        print(response.status_code)
        print(response.content)

    def test_category_post(self):
        response = self.client.post(reverse('api_ecomm:category'), {
            'name': 'cat 3',
            'level': 4,
            'parent_cat':1,
        })
        print(response.status_code)
        print(response.content)
