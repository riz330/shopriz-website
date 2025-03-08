from email import message
from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse('This Is My HomePage')
    messages.success(request,"This Is Test Message")
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')
    
    # return HttpResponse('This Is My  About Page')


def service(request):
    return render(request,'services.html')
    # return HttpResponse('This Is My  Service Page')

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        contact=Contact(name=name,email=email,subject=subject,message=message,date=datetime.today())
        contact.save()
        messages.success(request,"Your Message Has Been Sent!")

    
    return render(request,'contact.html')
    # return HttpResponse('This Is My  Contact Page')