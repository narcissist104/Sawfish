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
        return redirect('/view_request_form')

    return render(request, 'student_request_form.html', {'form':form})

def view_request_form(request):

    requests = Request.objects.all()

    return render(request, 'view_request_form.html',{'requests':requests})

def student_edit_request(request, request_id):
    req = Request.objects.get(id=request_id)

    form = Student_Request_Form(instance=req)

    if request.method == 'POST':

        form = Student_Request_Form(request.POST, instance=req)
        
        if form.is_valid():
            form.save()
        return redirect('/view_request_form')

    return render(request, 'student_edit_request.html', {'form':form})

def student_delete_request(request, request_id):

    req = Request.objects.get(id=request_id)

    if request.method == 'POST':
        req.delete()
        return redirect('/view_request_form')

    return render(request, 'student_delete_request.html', {'req':req}) 