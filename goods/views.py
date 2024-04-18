from unicodedata import category
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from goods.models import Categories, Products, СonditionsItemCategory
from main.models import New


# Create your views here.


def catalog(request, slug):
    cat = get_object_or_404(Categories, slug=slug)
    if slug == "vse-kategorii":
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=slug)) 
    context = {
        "title": "Catalog",
        "goods": goods,
        "cat": cat,
    }
    return render(request, "goods/catalog.html", context=context)

def product(request, slug):
    product = Products.objects.get(slug=slug)
    conditions = СonditionsItemCategory.objects.prefetch_related('details')
    new = New.objects.all().first()
    news = Products.objects.filter(is_new=True)
    context = {
        "title": "Product-name",
        "product": product, 
        "conditions": conditions,
        "new": new,
        "news": news     
    }
    return render(request, "goods/product.html", context=context)