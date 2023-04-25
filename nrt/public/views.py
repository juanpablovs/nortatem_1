from django.shortcuts import render

def index(request):
    return render(request, 'public/index.html')

def legal(request):
    return render(request, 'public/legal.html')