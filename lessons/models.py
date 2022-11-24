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


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    def __str__(self):
        return str(self.name)

class Admin(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    def __str__(self):
        return str(self.name)

class Director(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    def __str__(self):
        return str(self.name)

class Invoice(models.Model):
    invoiceNum = models.CharField(max_length=30)
    referNum = models.CharField(max_length=30)
    def __str__(self):
        return str(self.invoiceNum)

class Lessons(models.Model):
    title = models.CharField(max_length=20)
    duration = models.IntegerField()
    student_id = models.CharField(max_length=30)
    teacher_id = models.CharField(max_length=30)
    def __str__(self):
        return str(self.title)

class Requests(models.Model):
    student_id = models.CharField(max_length=30)
    # Store the availability as a reference to the dates within the availability database
    duration = models.IntegerField()
    # Interval stored as how many times per week
    interval = models.IntegerField()
    topic = models.CharField(max_length=20, default="")
    teacher_id = models.CharField(max_length=30, default="")

# Stores the dates in the availability database.
class Availability(models.Model):
    request_id = models.CharField(max_length=30, default="")
    date = models.DateField()
