import unittest

from app.dialogs.windows.login.auth import generate_code_verifier, get_access_token


class TestAuthGenerator(unittest.TestCase):
    def test_uniqueness(self):
        code_verifier1 = generate_code_verifier()
        code_verifier2 = generate_code_verifier()
        self.assertNotEqual(code_verifier1, code_verifier2)


class TestAuth(unittest.TestCase):
    def test_error_handling(self):
        with self.assertRaises(ValueError):
            get_access_token("wrong", "wrong")
