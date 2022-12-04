from django import forms
from .models import Request

class Student_Request_Form(forms.ModelForm):
    
    class Meta:
        model = Request
        fields = ['instrument', 'availibility', 'number_of_lessons', 'interval', 'duration', 'teacher']
        
        


