from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def second(request):
    return render(request, 'second.html')

def createpac(request):
    return render(request, 'createpac.html')

def createmed(request):
    return render(request, 'createmed.html')

def createcons(request):
    return render(request, 'createcons.html')

def readpac(request):
    return render(request, 'readpac.html')

def readmed(request):
    return render(request, 'readmed.html')
