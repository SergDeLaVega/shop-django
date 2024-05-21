from os import name
from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:slug>/', views.catalog, name='catalog'),
    path('product/<slug:slug>/', views.product, name='product')
]