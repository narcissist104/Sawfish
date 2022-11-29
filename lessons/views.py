from django.shortcuts import render

# Create your views here.

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def student_request_form(request):
    return render(request, 'student_request_form.html')

def view_request_form(request):
    return render(request, 'view_request_form.html')