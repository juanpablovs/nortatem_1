from django.shortcuts import render

navbar = {'titulo': 'el uno', 'otro': 'el dos'}
footer = {}

def index(request):
    return render(request, 'public/index.html', {
        'page_title': 'NORTATEM | Welcome',
        'page_css': 'public/css/index.css', #optional
        'page_js': 'public/js/index.js', #optional
        'page_keywords': 'NORTATEM, B2B marketplace, chatGPT, language model, machine learning, wholesalers, distributors, sellers, purchasing managers, sales, B2B sales, find B2B buyers, find B2B suppliers, machine learning, automated sales, artificial intelligence',
        'page_description': 'Looking to increase margins via sales or purchasing? With more than 7,000,000 companies from all over the world we automatize the tedious parts of selling and buying. Works from day 1. No training required',
        'navbar': navbar,
        'footer': footer,
    })

def legal(request):
    return render(request, 'public/legal.html')