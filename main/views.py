from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('Hpme Page')

def about(request):
    return HttpResponse('About Page')
