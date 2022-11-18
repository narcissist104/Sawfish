from django.db import models

# Create your models here.
class Student(models.Model):
    # REQUIRED_FIELDS = ('name','email', 'password')
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    def __str__(self):
        return str(self.name)