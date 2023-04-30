from django.test import TestCase, Client
import json


class IndexTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_get_index_endpoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        context = json.loads(response.content)
        self.assertEqual(context, {
            "text": "starting page"
        })
