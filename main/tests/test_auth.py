import json
from django.test import TestCase, Client


class AuthTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def signup(self):
        return self.client.post("/signup", data={"username": "vasya",
                                                 "password": "promprog"})

    def logout(self, token):
        return self.client.post("/logout", headers={"Authorization": f"Token {token}"})

    def test_running(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.signup()
        context: dict = json.loads(response.content)
        self.assertIn("token", context.keys())

    def test_double_register(self):
        self.signup()
        response = self.signup()
        context: dict = json.loads(response.content)
        self.assertEqual(context, {
            "username": [
                "A user with that username already exists."
            ]
        })

    def test_good_logout(self):
        response = self.signup()
        context = json.loads(response.content)
        token = context["token"]
        response = self.logout(token)
        self.assertEqual(response.data, "successful")

    def test_bad_logout(self):
        response = self.logout("token")
        context = json.loads(response.content)
        self.assertEqual(context, {
            "detail": "Invalid token."
        })

    def test_good_login(self):
        response = self.signup()
        context = json.loads(response.content)
        token1 = context["token"]
        self.logout(token1)
        response = self.client.post("/login", data={
            "username": "vasya",
            "password": "promprog",
        })
        self.assertEqual(response.status_code, 200)

    def test_bad_login_1(self):
        response = self.signup()
        context = json.loads(response.content)
        token1 = context["token"]
        self.logout(token1)
        response = self.client.post("/login", data={
            "username": "vasya",
            "password": "promprog123",
        })
        context = json.loads(response.content)
        self.assertEqual(context, {
            "detail": "Bad password"
        })

    def test_bad_login_2(self):
        response = self.signup()
        context = json.loads(response.content)
        token1 = context["token"]
        self.logout(token1)
        response = self.client.post("/login", data={
            "username": "vasya12",
            "password": "promprog",
        })
        context = json.loads(response.content)
        self.assertEqual(context, {
            "detail": "Not found."
        })
