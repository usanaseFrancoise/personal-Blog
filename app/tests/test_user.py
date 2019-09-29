import unittest
from app.models import User

class UserModelTest(unittest,TestCase):
    def setUp(self):
        self.new_user=User(password='havugima@2019')

    def test_password_setter(self):
        self.asserTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.asserTrue(Self,new_user.verify_password('havugima@2019'))