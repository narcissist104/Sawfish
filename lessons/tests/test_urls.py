from django.test import SimpleTestCase
from django.urls import reverse, resolve
from lessons.views import home, log_in, sign_up, student_dashboard, student_request_form, view_request_form, admin_dashboard, manage_requests, delete_requests, edit_requests, director_dashboard, manage_accounts, create_account, edit_account, delete_account
#from lessons.admin.site import urls

class TestURLS(SimpleTestCase):

    # This test does not work. How do we test admin urls?
    """ '''Ensure admin url redirects to the admin page'''
    def test_admin_url_is_resolved(self):
        url = reverse('admin_url')
        print(resolve(url))
        self.assertEquals(resolve(url).func, urls) """

    '''Ensure home url redirects to the home page'''
    def test_home_url_is_resolved(self):
        url = reverse('home_url')
        self.assertEquals(resolve(url).func, home)

    '''Ensure log-in url redirects to the log-in page'''
    def test_log_in_url_is_resolved(self):
        url = reverse('log_in_url')
        self.assertEquals(resolve(url).func, log_in)

    '''Ensure sign-up url redirects to the sign-up page'''
    def test_sign_up_url_is_resolved(self):
        url = reverse('sign_up_url')
        self.assertEquals(resolve(url).func, sign_up)
    
    # URLs for Student
    '''Ensure student dashboard url redirects to the student dashboard page'''
    def test_student_dashboard_url_is_resolved(self):
        url = reverse('student_dashboard')
        self.assertEquals(resolve(url).func, student_dashboard)

    def test_view_request_form_url_is_resolved(self):
        url = reverse('student_request_form')
        self.assertEquals(resolve(url).func, student_request_form)

    def test_student_request_form_url_is_resolved(self):
        url = reverse('student_request_form')
        self.assertEquals(resolve(url).func, student_request_form)

    def test_view_request_form_url_is_resolved(self):
        url = reverse('view_request_form')
        self.assertEquals(resolve(url).func, view_request_form)
    
    # URLs for Admins
    def test_admin_dashboard_url_is_resolved(self):
        url = reverse('admin_dashboard')
        self.assertEquals(resolve(url).func, admin_dashboard)
    
    def test_manage_requests_url_is_resolved(self):
        url = reverse('manage_requests')
        self.assertEquals(resolve(url).func, manage_requests)
    
    def test_edit_requests_url_is_resolved(self):
        url = reverse('edit_requests', args=['request_id'])
        self.assertEquals(resolve(url).func, edit_requests)
    
    def test_delete_requests_url_is_resolved(self):
        url = reverse('delete_requests', args=['request_id'])
        self.assertEquals(resolve(url).func, delete_requests)
    
    # URLs for Directors
    def test_director_dashboard_url_is_resolved(self):
        url = reverse('director_dashboard')
        self.assertEquals(resolve(url).func, director_dashboard)

    def test_manage_accounts_url_is_resolved(self):
        url = reverse('manage_accounts')
        self.assertEquals(resolve(url).func, manage_accounts)

    def test_create_account_url_is_resolved(self):
        url = reverse('create_account')
        self.assertEquals(resolve(url).func, create_account)

    def test_edit_account_url_is_resolved(self):
        url = reverse('edit_account', args=['account_id'])
        self.assertEquals(resolve(url).func, edit_account)

    def test_delete_account_url_is_resolved(self):
        url = reverse('delete_account', args=['account_id'])
        self.assertEquals(resolve(url).func, delete_account)