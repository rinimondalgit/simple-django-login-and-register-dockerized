from django.test import TestCase


class AccountPageTests(TestCase):
    def test_login_page_loads(self):
        response = self.client.get("/accounts/log-in/")
        self.assertEqual(response.status_code, 200)

    def test_signup_page_loads(self):
        response = self.client.get("/accounts/sign-up/")
        self.assertEqual(response.status_code, 200)

    def test_restore_password_page_loads(self):
        response = self.client.get("/accounts/restore/password/")
        self.assertEqual(response.status_code, 200)