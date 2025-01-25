import unittest
from password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        generator = PasswordGenerator(lower=5, upper=5, digits=5, specials=5)
        password = generator.generate_password()
        print(f"Generated password: {password}")
        self.assertEqual(len(password), 20)

    def test_password_composition(self):
        generator = PasswordGenerator(lower=2, upper=2, digits=2, specials=2)
        password = generator.generate_password()
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for c in password))
