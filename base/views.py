from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings
# Create your views here.

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def post(request):
    context = {}
    return render(request, 'base/post.html', context)

# def sendEmail(request):

#     if request.method == 'POST':

#         template = render_to_string('base/email_template.html', {
#             'name':request.POST['name'],
#             'email':request.POST['email'],
#             'message':request.POST['message'],
#         })
#         email = EmailMessage(
#             request.POST['subject'],
#             template,
#             settings.EMAIL_HOST_USER,
#             ['bob1233213123@gmail.com']
#         )
#         email.fail_silently=False
#         email.send()

#     return HttpResponse('Email was sent')
