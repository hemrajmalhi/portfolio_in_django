from django.shortcuts import render, redirect
from myportfolio.models import Contact
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "home.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message)
        if len(name) < 4 or len(email) < 10 or len(subject) < 5 or len(message) < 6:
            messages.error(request,"Please fill this form completely")
        else:
            contact.save()
            messages.success(request, "your message has been Successfully sent")
    return redirect('home')
