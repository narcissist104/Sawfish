from django.db import models

# Create your models here.
class Request(models.Model):

    instrument = models.CharField(max_length=20)

    availibility = models.DateField('enter your start time for the lessons (yyyy-mm-dd)', null=True)
    
    number_of_lessons = models.IntegerField()

    interval = models.IntegerField()

    SELVALUE_DURATION = (
        ('30','30 minutes'),
        ('45','45 minutes'),
        ('60','60 minutes'),        
    )
    duration = models.CharField(max_length=10, choices=SELVALUE_DURATION)

    teacher = models.CharField(max_length=20)

    


