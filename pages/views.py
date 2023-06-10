from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contract(request):
    return render(request, 'pages/contract.html')
