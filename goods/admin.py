from django.contrib import admin
from goods.models import Categories, Products, ProductImage, СonditionsItemCategory, СonditionsItemDetail, Feature, FeatureValue
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ProductAdmin(forms.ModelForm):
    full_description = forms.CharField(widget=CKEditorUploadingWidget())
    features = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Products
        fields = '__all__'

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]

class FeatureValueInline(admin.TabularInline):
    model = FeatureValue
    extra = 1

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [FeatureValueInline]

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    # ... другие настройки админ-класса для продукта
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "price", "discount", "is_best_seller", "is_new", ]
    list_editable = ["discount",]
    search_fields = ["name", "brief_description"]
    list_filter = ["discount", "quantity", "category"]
    fields = [
        "name",
        "category",
        "slug",
        "brief_description",
        "full_description",
        "features",
        ("price", "discount"),
        "quantity",
        "is_best_seller", 
        "is_new", 
        "video", 
        "local_video",
        "feature_values",
    ]
    filter_horizontal = ('feature_values',)  # Это добавляет поле с возможностью выбора нескольких значений характеристик
    form = ProductAdmin



admin.site.register(Products, ProductAdmin)

class СonditionsItemDetailInline(admin.TabularInline):  # Или использовать admin.StackedInline для другой компоновки
    model = СonditionsItemDetail
    extra = 1  # Количество пустых форм для новых объектов

@admin.register(СonditionsItemCategory)
class СonditionsItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']  # Поля для отображения в списке
    inlines = [СonditionsItemDetailInline]







