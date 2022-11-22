from django.db import models

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
