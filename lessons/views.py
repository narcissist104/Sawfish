from django.shortcuts import render
from .forms import Student_Request_Form
from .models import Lesson

# Create your views here. 

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def student_request_form(request):
    if request.method == 'POST':
        form = Student_Request_Form(request.POST)
    else:
        form = Student_Request_Form()
    return render(request, 'student_request_form.html',{'form':form})

def view_request_form(request):
    lessons = Lesson.objects.all()
    return render(request, 'view_request_form.html',{'lessons':lessons})

