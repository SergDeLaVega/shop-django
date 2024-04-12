from unicodedata import category
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, render
from goods.models import Products, СonditionsItemCategory


# Create your views here.


def catalog(request, slug):
    if slug == "vse-kategorii":
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=slug)) 
    context = {
        "title": "Catalog",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context=context)

def product(request, slug):
    product = Products.objects.get(slug=slug)
    conditions = СonditionsItemCategory.objects.prefetch_related('details')
    context = {
        "title": "Product-name",
        "product": product, 
        "conditions": conditions     
    }
    return render(request, "goods/product.html", context=context)