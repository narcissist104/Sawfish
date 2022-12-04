from django.shortcuts import redirect, render
from .forms import LogInForm, SignUpForm, EditRequestForm
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Request

from django.shortcuts import render
from .forms import Student_Request_Form
from .models import Lesson

# Create your views here.
def home(request):
    return render(request, 'home.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('feed')
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})


def admin_requests(request):
    requests = Request.objects.all()
    return render(request, 'admin_requests.html', {'requests': requests})


def admin_edit_requests(request, request_id):
    if request.method == 'POST':
        form = EditRequestForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data.get('student_id')
            duration = form.cleaned_data.get('duration')
            interval = form.cleaned_data.get('interval')
            topic = form.cleaned_data.get('topic')
            teacher_id = form.cleaned_data.get('teacher_id')
            req = Request.objects.filter(id=request_id).update(student_id=student_id, duration=duration,
                                                               interval=interval, topic=topic, teacher_id=teacher_id)
            return redirect('http://localhost:8000/admin_requests/')
    form = EditRequestForm()
    return render(request, 'admin_edit_requests.html', context={'request': request_id, 'form': form})

def admin_delete_requests(request, request_id):
    if request.method == 'POST':
        requests = Request.objects.get(id=request_id).delete()
        return redirect('http://localhost:8000/admin_requests/')
    return render(request, 'admin_delete_requests.html', context={'request': request_id})

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

