from django.shortcuts import render

def home(request):
    return render(request,'aplicacion/home.html')

def other(request):
    return render(request,'aplicacion/other.html')
