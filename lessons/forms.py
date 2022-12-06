from django import forms
from .models import Request

class Student_Request_Form(forms.ModelForm):
    """Form enabling student to request a lesson"""
    class Meta:
        model = Request
        fields = ['instrument', 'availibility', 'number_of_lessons', 'interval', 'duration', 'teacher']

        


