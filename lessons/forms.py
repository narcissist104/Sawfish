"""Forms for the microblogs app."""
from django import forms
from django.core.validators import RegexValidator
from .models import User, Lesson, Request

class LogInForm(forms.Form):
    """Form enabling registered users to log in."""

    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())


class SignUpForm(forms.ModelForm):
    """Form enabling unregistered users to sign up."""

    class Meta:
        """Form options."""

        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'bio']
        widgets = { 'bio': forms.Textarea() }

    new_password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        validators=[RegexValidator(
            regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
            message='Password must contain an uppercase character, a lowercase '
                    'character and a number'
            )]
    )
    password_confirmation = forms.CharField(label='Password confirmation', widget=forms.PasswordInput())

    def clean(self):
        """Clean the data and generate messages for any errors."""

        super().clean()
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if new_password != password_confirmation:
            self.add_error('password_confirmation', 'Confirmation does not match password.')

    def save(self):
        """Create a new user."""

        super().save(commit=False)
        user = User.objects.create_user(
            self.cleaned_data.get('username'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            email=self.cleaned_data.get('email'),
            bio=self.cleaned_data.get('bio'),
            password=self.cleaned_data.get('new_password'),
        )
        return user

class EditRequestForm(forms.Form):
    """Form enabling request edits by admins"""
    student_id = forms.IntegerField(label="student_id")
    duration = forms.IntegerField(label="duration")
    interval = forms.IntegerField(label="availability")
    topic = forms.CharField(label="topic")
    teacher_id = forms.IntegerField(label="teacher_id")

class EditAccount(forms.Form):
    """Form enabling request edits by admins"""
    username = forms.CharField(label="username")
    first_name = forms.CharField(label="first_name")
    last_name = forms.CharField(label="last_name")
    email = forms.EmailField(label="email")
    bio = forms.CharField(label="bio")
    SELVALUE_LESSON = (
            ('student','student'),
            ('admin','admin'),
            ('director','director'),
        )
    type = forms.CharField(max_length=20, widget=forms.widgets.Select(choices=SELVALUE_LESSON))
    def save(self):
        """Create a new user."""
        user = User.objects.create_user(
            self.cleaned_data.get('username'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            email=self.cleaned_data.get('email'),
            bio=self.cleaned_data.get('bio'),
            password=self.cleaned_data.get('new_password'),
        )
        return user

class Student_Request_Form(forms.ModelForm):
    
    class Meta:
        model = Lesson
        fields = ['instrument', 'number_of_lessons', 'interval', 'duration', 'teacher_id']
        

    """SELVALUE_LESSON = (
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


    teacher = forms.CharField(max_length=20)"""
        


