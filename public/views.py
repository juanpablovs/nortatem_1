from django.shortcuts import render

def index(response):
    return render(response, 'public/index.html', {'page_title': 'NORTATEM | Welcome',
    })