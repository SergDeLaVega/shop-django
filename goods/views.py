from pyexpat import features
from unicodedata import category
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from goods.models import Categories, Products, СonditionsItemCategory, Feature, FeatureValue
from main.models import New
from django.db.models import Count, Q
from collections import Counter


# Create your views here.


def catalog(request, slug):
    # Получаем страницу и параметры для сортировки и пагинации
    page = request.GET.get('page', 1)
    sort = request.GET.get('sort', '') # Добавлено для сортировки
    show = request.GET.get('show', 9) # Добавлено для количества товаров на странице

    # Получаем список выбранных значений фильтра из запроса
    selected_features = request.GET.getlist('features')

    #Получение значени характеристик товара для вывода сайтбара фильтрации по характеристикам
    features = Feature.objects.prefetch_related('values__products').annotate(num_products=Count('values__products')).filter(num_products__gt=0)
    
    cat = get_object_or_404(Categories, slug=slug)
    if slug == "vse-kategorii":
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=slug)

    # Фильтрация товаров по выбранным характеристикам
    #if selected_features:
        #goods = goods.filter(feature_values__id__in=selected_features).distinct()
    # Фильтрация товаров по выбранным характеристикам
    if selected_features: 
        queries = [Q(feature_values__id=value_id) for value_id in selected_features] 
        query = queries[0]  # Сохраняем первый Q-объект, не делаем .pop()

        for item in queries[1:]:  # Начинаем с первого элемента после первого
            query &= item  # Добавляем остальные значения через оператор И
            print(query)
        goods = goods.filter(query).distinct()  # Фильтруем товары
        print(goods)

    # Применение фильтрации и сортировки
    if sort == '1':
        goods = goods.order_by('name')
    elif sort == '2':
        goods = goods.order_by('-name')
    elif sort == '3':
        goods = goods.order_by('price')
    elif sort == '4':
        goods = goods.order_by('-price') 

    # Применение пагинатора с учетом количества товаров на странице
    paginator = Paginator(goods, int(show))
    current_page = paginator.page(int(page))

    context = {
        "title": "Catalog",
        "cat": cat,
        "goods": current_page,
        "features": features,
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
        "news": news,
    }
    return render(request, "goods/product.html", context=context)