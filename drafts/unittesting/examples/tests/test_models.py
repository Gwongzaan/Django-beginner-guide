from django.test import TestCase
from examples.models import MyModel


class MyModelTestCase(TestCase):
    def setUp(self):
        # set up initial data for the tests
        MyModel.objects.create(name="Test Item", value=42)

    def test_model_createion(self):
        """
        Test Model creation works correctly
        """
        item = MyModel.objects.get(name="Test Item")
        self.assertEqual(item.value, 42)
