from django.shortcuts import render, redirect
from .forms import Student_Request_Form
from .models import Lesson


# Create your views here. 

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def student_request_form(request):

    form = Student_Request_Form()

    if request.method == 'POST':

        form = Student_Request_Form(request.POST)

        if form.is_valid():
            """requested_instrument = form.cleaned_data.get('instrument')
            requested_number_of_lessons = form.cleaned_data.get('number_of_lessons')
            requested_interval = form.cleaned_data.get('interval')
            requested_duration = form.cleaned_data.get('duration')
            requested_teacher = form.cleaned_data.get('teacher')"""
            form.save()
            
    
    return render(request, 'student_request_form.html', {'form':form})


def view_request_form(request):
    lessons = Lesson.objects.all()
    return render(request, 'view_request_form.html',{'lessons':lessons})

