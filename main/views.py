from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "title": "Home"
    }
    return render(request, "main/index.html", context=context)

def about(request):
    context = {
        "title": "О нас",
        "content": "Страница о нас",
        "text": "Небольшое описание о том кто мы такие"

    }
    return render(request, "main/about.html", context=context)
