from django.shortcuts import render

def index(response):
    return render(response, 'agent/index.html')