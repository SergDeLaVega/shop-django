from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from goods.models import Products
from .models import About, Advantage,  Slider, Map, Hit, New, Contact, Pyment, Delivery

# Create your views here.


def index(request):
    slides = Slider.objects.filter(is_active=True)
    advanteges = Advantage.objects.all()
    about = About.objects.all().first()
    maps = Map.objects.all()
    hit = Hit.objects.all().first()
    hits = Products.objects.filter(is_best_seller=True)
    new = New.objects.all().first()
    news = Products.objects.filter(is_new=True)
    context = {
        "title": "Home",
        'slides': slides,
        'advanteges': advanteges,
        "about": about,
        "maps": maps,
        "hit": hit,
        "hits": hits,
        "new": new,
        "news": news,
    }
    return render(request, "main/index.html", context=context)

def about(request):
    about = About.objects.all().first()
    context = {
        "title": "О нас",
        "about": about,
    }
    return render(request, "main/about.html", context=context)

def contact(request):
    contact = Contact.objects.all().first()
    context = {
        "title": "О нас",
        "contact": contact,
    }
    return render(request, "main/contact.html", context=context)

def pyment(request):
    pyment = Pyment.objects.all().first()
    context = {
        "title": "О нас",
        "pyment": pyment,
    }
    return render(request, "main/pyment.html", context=context)

def delivery(request):
    delivery = Delivery.objects.all().first()
    context = {
        "title": "О нас",
        "delivery": delivery,
    }
    return render(request, "main/delivery.html", context=context)
