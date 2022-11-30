from django import forms
from .models import Lesson

class Student_Request_Form(forms.Form):
    class Meta:
        model = Lesson

    SELVALUE_LESSON = (
        ('violin','violin'),
        ('piano','piano'),
        ('giutar','guitar'),
    )
    lesson = forms.CharField(max_length=20, widget=forms.widgets.Select(choices=SELVALUE_LESSON))
    
    SELVALUE__NUMBER_OF_LESSONS = (
        ('24','24'),
        ('48','48'),
        ('72','72'),
        ('96','96'),
    )
    number_of_lessons = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=SELVALUE__NUMBER_OF_LESSONS))

    SELVALUE_INTERVAL = (
        ('1','1 lesson every week'),
        ('2','2 lessons every week'),
    )
    interval = forms.CharField(max_length=20, widget=forms.widgets.Select(choices=SELVALUE_INTERVAL))

    SELVALUE_DURATION = (
        ('30','30 minutes'),
        ('45','45 minutes'),
        ('60','60 minutes'),        
    )
    duration = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=SELVALUE_DURATION))


    teacher = forms.CharField(max_length=20)


