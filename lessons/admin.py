from django.contrib import admin

# Register your models here.
from .models import Student, Teacher, Director, Invoice

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

@admin.register(Teacher)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoiceNum', 'referNum')