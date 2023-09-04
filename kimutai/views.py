from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.core.mail import EmailMessage,BadHeaderError
from django.contrib import messages
from .models import Contact
import requests
# from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        message= request.POST.get('message')

        api_key= 'f9b6a58f27c74c1aadf2506412e266f9'
        url = f'https://api.zerobounce.net/v2/validate?apikey={api_key}&email={email}'
        
        try:
            response = requests.get(url)
            print(response.text)
            data = response.json()
            is_valid= data.get('status') == 'valid'
            
            if not is_valid:
                message.error(request, 'Please Enter a valid Email')

            subject= f'Contact submission form {name}'

            emailmessage= EmailMessage(
                subject,
                f'Name: {name}\nMessage: {message}',
                'senorfetty@gmail.com',
                ['billykimbett@gmail.com'],
                reply_to = [email],
            )    
            emailmessage.send()
            messages.success(request, "Message Sent! 💌 We'll be in Touch Soon!")
            return redirect(reverse('home') + '#contact')
        
        except Exception as e:
            return JsonResponse({'error': str(e)})
            
    
    else:
        return render (request, 'index.html')
