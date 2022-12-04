from django.contrib import admin

# Register your models here.
from .models import User, Student, Admin, Director, Invoice, Lesson, Request, Availability

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'bio', 'type')


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoiceNum', 'referNum')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("student_id", "instrument", "number_of_lessons", "interval", "duration", "teacher_id")

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ("student_id", "duration", "interval", "topic", "teacher_id")

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("request_id", "date")