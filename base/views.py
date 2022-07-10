from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def post(request):
    context = {}
    return render(request, 'base/post.html', context)