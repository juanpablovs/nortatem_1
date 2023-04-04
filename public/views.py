from django.shortcuts import render

def index(response):
    return render(response, 'public/index.html', {
        'page_title': 'NORTATEM | Welcome',
        'page_keywords': 'sales, B2B sales, find B2B buyers, find B2B suppliers, machine learning, automated sales, artificial intelligence',
        'page_description': 'Looking to increase margins via sales or purchasing? With more than 7,000,000 companies from all over the world we automatize the tedious parts of selling and buying. Works from day 1. No training required',
    })