from django.test import TestCase
from django.urls import reverse


class MyViewTestCase(TestCase):
    """
    This information will be displayed when running the test
    """

    def test_index_view(self):
        response = self.client.get(reverse("examples:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome")
