from django.shortcuts import redirect, render
from .forms import LogInForm, SignUpForm, EditRequestForm, EditAccount
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Request, User

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
            return redirect('http://localhost:8000/')
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
                if user.type == "admin":
                    return redirect('http://localhost:8000/admin_dashboard')
                elif user.type == "director":
                    return redirect('http://localhost:8000/director_dashboard')
                else:
                    return redirect('http://localhost:8000/student_dashboard')
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})

@login_required
def admin_dashboard(request):
    if request.user.type == "student":
        return redirect('http://localhost:8000/student_dashboard')
    return render(request, 'admin_dashboard.html')
@login_required
def manage_requests(request):
    if request.user.type == "student":
        return redirect('http://localhost:8000/student_dashboard')
    requests = Request.objects.all()
    return render(request, 'manage_requests.html', {'requests': requests})


@login_required
def edit_requests(request, request_id):
    req = Request.objects.get(id=request_id)
    if request.user.type == "student":
        return redirect('http://localhost:8000/student_dashboard')
    if request.method == 'POST':
        form = EditRequestForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data.get('student_id')
            duration = form.cleaned_data.get('duration')
            interval = form.cleaned_data.get('interval')
            topic = form.cleaned_data.get('topic')
            teacher_id = form.cleaned_data.get('teacher_id')
            req.update(student_id=student_id, duration=duration,
                                                               interval=interval, topic=topic, teacher_id=teacher_id)
            return redirect('http://localhost:8000/admin_requests/')
    form = EditRequestForm()
    return render(request, 'edit_request.html', context={'request': req, 'form': form})


@login_required
def delete_requests(request, request_id):
    if request.user.type == "student":
        return redirect('http://localhost:8000/student_dashboard')
    if request.method == 'POST':
        requests = Request.objects.get(id=request_id).delete()
        return redirect('http://localhost:8000/admin_requests/')
    return render(request, 'delete_request.html', context={'request': request_id})


def student_dashboard(request):
    return render(request, 'student_dashboard.html')


def student_request_form(request):

    form = Student_Request_Form()

    if request.method == 'POST':

        form = Student_Request_Form(request.POST)

        if form.is_valid():
            # requested_instrument = form.cleaned_data.get('instrument')
            # requested_number_of_lessons = form.cleaned_data.get('number_of_lessons')
            # requested_interval = form.cleaned_data.get('interval')
            # requested_duration = form.cleaned_data.get('duration')
            # requested_teacher = form.cleaned_data.get('teacher')
            form.save()
            return redirect('http://localhost:8000/student_dashboard')
    return render(request, 'student_request_form.html', {'form':form})


def view_request_form(request):
    lessons = Request.objects.filter(student_id=request.user.id)
    return render(request, 'view_request_form.html', {'lessons': lessons})
@login_required
def director_dashboard(request):
    if request.user.type != "director":
        return redirect('http://localhost:8000/')
    return render(request, 'director_dashboard.html')
@login_required
def manage_accounts(request):
    if request.user.type != "director":
        return redirect('http://localhost:8000/')
    accounts = User.objects.all()
    return render(request, 'manage_accounts.html', {'accounts': accounts})

@login_required
def delete_account(request, account_id):
    if request.user.type != "director":
        return redirect('http://localhost:8000/')
    if request.method == 'POST':
        requests = User.objects.get(id=account_id).delete()
        return redirect('http://localhost:8000/director_dashboard/')
    return render(request, 'delete_account.html', context={'request': account_id})

@login_required
def create_account(request):
    if request.user.type != "director":
        return redirect('http://localhost:8000/')
    if request.method == 'POST':
        form = EditAccount(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://localhost:8000/director_dashboard/')
    form = EditAccount()
    return render(request, 'add_account.html', context={'form': form})

@login_required
def edit_account(request, account_id):
    if request.user.type != "director":
        return redirect('http://localhost:8000/')
    if request.method == 'POST':
        form = EditAccount(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            bio = form.cleaned_data.get('bio')
            type = form.cleaned_data.get('type')
            req = Request.objects.filter(id=account_id).update(username=username, first_name=first_name,
                                                               last_name=last_name, email=email, bio=bio, type=type)
            return redirect('http://localhost:8000/director_dashboard/')
    form = EditAccount()
    return render(request, 'edit_account.html', context={'request': account_id, 'form': form})