from django.test import TestCase


class TestCartURL(TestCase):

    def test_cart_page_url(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
