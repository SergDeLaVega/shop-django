from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "main/index.html")

def about(request):
    return HttpResponse('About Page')
