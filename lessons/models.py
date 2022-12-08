from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from libgravatar import Gravatar

class User(AbstractUser):
    """User model used for authentication and microblog authoring."""

    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[RegexValidator(
            regex=r'^@\w{3,}$',
            message='Username must consist of @ followed by at least three alphanumericals'
        )]
    )
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)
    bio = models.CharField(max_length=520, blank=True)
    type = models.CharField(max_length=15, default="student")

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def gravatar(self, size=120):
        """Return a URL to the user's gravatar."""
        gravatar_object = Gravatar(self.email)
        gravatar_url = gravatar_object.get_image(size=size, default='mp')
        return gravatar_url

    def mini_gravatar(self):
        """Return a URL to a miniature version of the user's gravatar."""
        return self.gravatar(size=60)
    def __str__(self):
        return str(self.username)

class Invoice(models.Model):
    invoiceNum = models.CharField(max_length=30)
    referNum = models.CharField(max_length=30)
    bank_id = models.CharField(max_length=30, default=0)
    def __str__(self):
        return str(self.invoiceNum)
class BankAccount(models.Model):
    balance = models.FloatField()

# Stores the dates in the availability database.
class Availability(models.Model):
    request_id = models.CharField(max_length=30, default="")
    date = models.DateField()
class Lesson(models.Model):
    student_id = models.CharField(max_length=20)

    SELVALUE_LESSON = (
        ('violin','violin'),
        ('piano','piano'),
        ('giutar','guitar'),
    )
    instrument = models.CharField(max_length=20, choices=SELVALUE_LESSON)
    number_of_lessons = models.IntegerField()
    interval = models.IntegerField()
    SELVALUE_DURATION = (
        ('30', '30 minutes'),
        ('45', '45 minutes'),
        ('60', '60 minutes'),
    )
    duration = models.CharField(max_length=10, choices=SELVALUE_DURATION)
    teacher_id = models.CharField(max_length=20)

class Request(models.Model):
    student_id = models.CharField(max_length=30)
    instrument = models.CharField(max_length=20)
    availability = models.DateField('enter your start time for the lessons (yyyy-mm-dd)', null=True)
    number_of_lessons = models.IntegerField()
    interval = models.IntegerField()
    SELVALUE_DURATION = (
        ('30','30 minutes'),
        ('45','45 minutes'),
        ('60','60 minutes'),
    )
    duration = models.CharField(max_length=10, choices=SELVALUE_DURATION)
    teacher_id = models.CharField(max_length=20)
