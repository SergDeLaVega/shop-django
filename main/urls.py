from os import name
from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('pyment/', views.pyment, name='pyment'),
    path('delivery/', views.delivery, name='delivery')
]