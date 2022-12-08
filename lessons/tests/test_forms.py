from django.test import SimpleTestCase
from lessons.forms import LogInForm, SignUpForm, EditAccount, Student_Request_Form
from lessons.models import User
import datetime

class TestForms(SimpleTestCase):

    def setUp(self):
        self.date = datetime.date(1997, 10, 19)

    # Log in form - this test is not complete.
    # def test_log_in_form_valid_data(self):
    #     form = LogInForm(data={
    #         'username': '@JohnDoe',
    #         'password': 'Password123'
    #     })

    #     self.assertTrue(form.is_valid())

    def test_log_in_form_no_data(self):
        form = LogInForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
    
    # Sign up form - this test is not complete.
    # def test_sign_up_form_valid_data(self):
    #     form = SignUpForm(data={
    #         'field.first_name': 'John',
    #         'field.last_name': 'Doe',
    #         'field.username': '@John',
    #         'field.email': 'anon@example.org',
    #         'field.bio': 'Hi, Im John.',
    #         'new_password': 'Password123'
    #     })
    
    #     self.assertTrue(form.is_valid())
    
    def test_sign_up_form_no_data(self):
        form = SignUpForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    # Edit request form - this test is not complete.
    # def test_edit_account_form_valid_data(self):
    #     form = EditAccount(data={
    #         'username': '@John',
    #         'first_name': 'John',
    #         'last_name': 'Doe',
    #         'email': 'anon@example.org',
    #         'bio': 'Hi, Im John',
    #         'SELVALUE_LESSON': ''
    #         'type': ''
    #         'password': ''
    #     })

    #    self.assertTrue(form.is_valid())

    def test_edit_account_form_no_data(self):
        form = EditAccount(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)

    # Edit student request form - this test is not complete.
    # def test_edit_student_request_form_valid_data(self):
    #     form = Student_Request_Form(data={
    #         'model': '',
    #         'fields.instrument': 'violin',
    #         'fields.availability': self.date,
    #         'fields.number_of_lessons': '5',
    #         'fields.interval': '5',
    #         'fields.duration': '60',
    #         'fields.teacher_id': '2',
    #     })

    #    self.assertTrue(form.is_valid())
    
    def test_edit_student_request_form_no_data(self):
        form = Student_Request_Form(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)