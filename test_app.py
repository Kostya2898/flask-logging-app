import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_successful_login(self):
        response = self.client.post('/login', json={
            "username": "admin",
            "password": "secret"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "Login successful")

    def test_invalid_login(self):
        response = self.client.post('/login', json={
            "username": "admin",
            "password": "wrong"
        })
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json()["message"], "Invalid credentials")

if __name__ == '__main__':
    unittest.main()
