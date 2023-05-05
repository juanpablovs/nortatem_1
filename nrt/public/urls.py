from django.urls import path

from . import views

app_name = 'public'

urlpatterns = [
    path('', views.index, name='index'),
    path('ceos/', views.ceos, name='ceos'),
    path('buyer/', views.buyer, name='buyer'),
    path('seller/', views.seller, name='seller'),
    path('government/', views.government, name='government'),
    path('agent/', views.agent, name='agent'),
    path('legal/', views.legal, name='legal'),
]
