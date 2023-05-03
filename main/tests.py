import json
from django.test import TestCase, Client


class IndexTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_get_index_endpoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        # context = json.loads(response.content)
        # self.assertEqual(context, {
        #     "text": "starting page"
        # })

    def test_bad_login(self):
        response = self.client.post("/auth/token/login/", data={"username": "vasya",
                                                                "password": "promprogg"})
        context = json.loads(response.content)
        self.assertEqual(context, {
            'non_field_errors': ['Unable to log in with provided credentials.']
        })

    def test_register(self):
        response = self.client.post("/auth/users/", data={
            "username": "vasya",
            "password": "promprog",
        })
        context = json.loads(response.content)
        self.assertEqual(context, {
            "email": "",
            "id": 1,
            "username": "vasya",
        })

    def test_good_login(self):
        self.test_register()
        response = self.client.post("/auth/token/login/", data={
            "username": "vasya",
            "password": "promprog",
        })
        context = json.loads(response.content)
        # self.assertEqual(context)
        self.assertIn("auth_token", context)
