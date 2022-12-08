from django.test import TestCase
from lessons.models import User

class TestModesl(TestCase):

    def setUp(self):
        self.student1 = User.objects.create(
            username='Johnny',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            bio="Hi, I'm John.",
            type='student'
        )

        

        