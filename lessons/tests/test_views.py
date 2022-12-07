from django.test import TestCase, Client
from django.urls import reverse
#from lessons.models import Student
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home_url')
        self.log_in_url = reverse('log_in_url')
        self.sign_up_url = reverse('sign_up_url')

    def test_home_page_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_log_in_page_GET(self):
        response = self.client.get(self.log_in_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'log_in.html')

    def test_sign_up_page_GET(self):
        response = self.client.get(self.sign_up_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'sign_up.html')