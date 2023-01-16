from django.shortcuts import render
from myportfolio.models import Contact


# Create your views here.
def home(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message)
        if len(name) < 4 or len(email) < 10 or len(subject) < 5 or len(message) < 6:
            context = {"error": "Error"}
        else:
            contact.save()
            context = {"message": name}
    return render(request, "home.html", context)
