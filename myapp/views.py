from django.shortcuts import render, redirect
from .models import Client
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def index(request):
    current_page = 'index'
    if request.method == 'POST':
        full_name = request.POST['full_name']
        contact = request.POST['contact']
        email = request.POST['email']
        message = request.POST['message']

        new_data = Client(full_name=full_name, contact=contact, email=email, message=message)
        new_data.save()

        subject = 'Potential client from your website'
        message = 'A new message has been sent. Check your admin pannel'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['jimnaughtsmhlanga@gmail.com','jimnaught91@gmail.com']
        send_mail(subject, message, from_email, recipient_list)         
        return render(request, 'thanks.html')
    return render(request, 'index.html', {'current_page':current_page})


def contact(request):
    current_page = 'contact'
    if request.method == 'POST':
        full_name = request.POST['full_name']
        contact = request.POST['contact']
        email = request.POST['email']
        message = request.POST['message']

        new_data = Client(full_name=full_name, contact=contact, email=email, message=message)
        new_data.save()

        subject = 'Potential client from your website'
        message = 'A new message has been sent. Check your admin pannel'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['jimnaughtsmhlanga@gmail.com','jimnaught91@gmail.com']
        send_mail(subject, message, from_email, recipient_list)        
        return render(request, 'thanks.html')
    return render(request, 'contact.html', {'current_page':current_page})


def clients(request):
    current_page = 'clients'
    return render(request, 'clients.html',{'current_page':current_page})


def ourwork(request):
    current_page = 'ourwork'
    return render(request, 'ourwork.html', {'current_page':current_page})


def about(request):
    current_page = 'about'
    return render(request, 'about.html',{'current_page':current_page})
