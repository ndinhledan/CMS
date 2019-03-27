from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def send(request):
    #return HttpResponse('HELLO WORLD')
    subject = 'Crisis Management'
    message = 'Please run. '
    email_from = 'crisismanagement901@gmail.com'
    recipient_list = ['crisismanagement901@gmail.com','crisismanagement901@hotmail.com',]

    send_mail( subject, message, email_from, recipient_list )
    return render(request,'posts/index.html')

    # at settings , put below #
#   EmailBackend = 'django.core.mail.backends.smtp.EmailBackend'
#   EMAIL_HOST = 'smtp.gmail.com'
#   EMAIL_USE_TLS = True
#   EMAIL_PORT = 587
#   EMAIL_HOST_USER = 'crisismanagement901@gmail.com'
#   EMAIL_HOST_PASSWORD = '1234Pass'