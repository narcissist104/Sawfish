from django.test import TestCase, Client
from django.urls import reverse
from lessons.models import User
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.log_in_url = reverse('log_in')
        self.profile_url = reverse('profile')
        self.log_out_url = reverse('log_out')
        self.sign_up_url = reverse('sign_up')
        self.admin_dashboard_url = reverse('admin_dashboard')
        self.manage_requests_url = reverse('manage_requests')

        self.student1 = User.objects.create(
            username='Johnny',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            bio="Hi, I'm John.",
            type='student'
        )

    # POST methods testing
    def test_home_page_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_sign_up_page_GET(self):
        response = self.client.get(self.sign_up_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'sign_up.html')

    def test_log_in_page_GET(self):
        response = self.client.get(self.log_in_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'log_in.html')

    def test_log_out_page_GET(self):
        response = self.client.get(self.log_out_url)
        self.assertEquals(response.status_code, 302) # Redirects user to home page.

    # def test_profile_page_GET(self):
    #     response = self.client.get(self.profile_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'base.html')
    #     self.assertTemplateUsed(response, 'profile.html')

    # def test_admin_dashboard_page_GET(self):
    #     response = self.client.get(self.admin_dashboard_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'admin_dashboard.html')

    # def test_manage_requests_page_GET(self):
    #     response = self.client.get(self.manage_requests_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'manage_requests.html')
    
    # def test_sign_up_POST_creates_new_user(self):
    #     response = self.client.post(self.sign_up_url), {

    #     }

    #     self.assertEqual
