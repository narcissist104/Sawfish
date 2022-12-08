from django.test import TestCase
from lessons.models import User

class TestModesl(TestCase):

    def setUp(self):
        pass

    def test_username_regex(self):
        self.assertRegex('@Johnny_', r'^@\w{3,}$')
        self.assertNotRegex('@Johnny^', r'^@\w{3,}$')
        self.assertNotRegex('Johnny_', r'^@\w{3,}$')

        
        