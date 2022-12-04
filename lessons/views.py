from django.shortcuts import render, redirect
from .forms import Student_Request_Form
from .models import Request

# Create your views here. 

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def student_request_form(request):

    form = Student_Request_Form()
    
    if request.method == 'POST':

        form = Student_Request_Form(request.POST)

        if form.is_valid():
            form.save()

    return render(request, 'student_request_form.html', {'form':form})


def view_request_form(request):
    requests = Request.objects.all()
    return render(request, 'view_request_form.html',{'requests':requests})


            