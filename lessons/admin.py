from django.contrib import admin

# Register your models here.
from .models import Student, Admin, Director, Invoice, Lesson, Request, Availability, BankAccount

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    display = 'balance'

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoiceNum', 'referNum', 'bankAccNo')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "student_id", "teacher_id")
@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    display = "date"

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ("student_id", "duration", "interval", "topic", "teacher_id")