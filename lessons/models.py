from django.db import models

# Create your models here.
class Lesson(models.Model):
    SELVALUE_LESSON = (
        ('violin','violin'),
        ('piano','piano'),
        ('giutar','guitar'),
    )
    select_lesson = models.CharField(max_length=20, choices=SELVALUE_LESSON)

    start_date = models.DateTimeField('enter your start time', null=True)

    SELVALUE__NUMBER_OF_LESSONS = (
        ('24','24'),
        ('48','48'),
        ('72','72'),
        ('96','96'),
    )
    number_of_lessons = models.CharField(max_length=10, choices=SELVALUE__NUMBER_OF_LESSONS)

    SELVALUE_INTERVAL = (
        ('1','1 lesson every week'),
        ('2','2 lessons every week'),
    )
    interval = models.CharField(max_length=20, choices=SELVALUE_INTERVAL)

    SELVALUE_DURATION = (
        ('30','30 minutes'),
        ('45','45 minutes'),
        ('60','60 minutes'),        
    )
    duration = models.CharField(max_length=10, choices=SELVALUE_DURATION)

    teacher = models.CharField(max_length=20)


