from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.core.mail import EmailMessage,BadHeaderError
from django.contrib import messages
from .models import Contact
# from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        message= request.POST.get('message')

        subject= f'Contact submission form {name}'

        emailmessage= EmailMessage(
            subject,
            f'Name: {name}\nMessage: {message}',
            'senorfetty@gmail.com',
            ['billykimbett@gmail.com'],
            reply_to = [email],
        )      
        try:
            emailmessage.send()
        except BadHeaderError:
            return HttpResponse('Fake')
        messages.success(request, "Message Sent! 💌 We'll be in Touch Soon!")
        return redirect(reverse('home') + '#contact')
    
    else:
        return render (request, 'home.html')
