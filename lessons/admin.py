from django.contrib import admin

# Register your models here.
from .models import User, Invoice, Lesson, Request, Availability, BankAccount

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'bio', 'type')


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoiceNum', 'referNum','bank_id')


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    display = 'balance'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("student_id", "instrument", "number_of_lessons", "interval", "duration", "teacher_id")


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ("student_id", "instrument", "availability", "number_of_lessons", "interval", "teacher_id")



@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("request_id", "date")