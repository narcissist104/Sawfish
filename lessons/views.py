from django.shortcuts import redirect, render
from .forms import LogInForm, SignUpForm
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Request


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
    req = Request.objects.filter(id=request_id)
    return render(request, 'admin_edit_requests.html', context={'request': req})
