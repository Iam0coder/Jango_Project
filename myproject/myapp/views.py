# myapp/views.py
from django.shortcuts import render

def index(request):
    data = {'caption': "CatDjango"}
    return render(request, 'myapp/index.html', data)

def new(request):
    return render(request, 'myapp/new.html')

def page3(request):
    return render(request, 'myapp/page3.html')

def page4(request):
    return render(request, 'myapp/page4.html')
