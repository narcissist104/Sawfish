from django.contrib import admin

# Register your models here.
from .models import Student, Admin, Director, Invoice, Lessons, Requests, Availability

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoiceNum', 'referNum')

@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "student_id", "teacher_id")

@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    list_display = ("student_id", "duration", "interval", "topic", "teacher_id")

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("request_id", "date")