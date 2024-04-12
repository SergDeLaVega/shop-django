from django.db import models
from django.urls import reverse



class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    brief_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание')
    features = models.TextField(verbose_name='Особенности')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Скидка', blank=True, null=True)
    quantity = models.IntegerField(verbose_name='Количество', default=0)
    is_best_seller = models.BooleanField(default=False, verbose_name='Хит продаж')
    is_new = models.BooleanField(default=False, verbose_name='Новинка')
    video = models.URLField(verbose_name='Видео', blank=True, null=True)
    local_video = models.FileField(upload_to='videos/', verbose_name='Видео', blank=True, null=True)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')


    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"slug": self.slug})
    

    def display_id(self):
        return f"{self.id:05}"


    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        
        return self.price


class ProductImage(models.Model):
    product = models.ForeignKey(Products, related_name='images', on_delete=models.CASCADE, verbose_name='Товар')
    image = models.ImageField(upload_to='product_images/', verbose_name='Изображение')
    alt_text = models.CharField(max_length=255, blank=True, verbose_name='Альтернативный текст')  # Для SEO и доступности

    def __str__(self):
        return f"Изображение для {self.product.name}"

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображения продуктов'


    
    
class СonditionsItemCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название пункта")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Условия: гарантия, доставкa, оплата'
        verbose_name_plural = 'Условия: гарантия, доставкa, оплата'

class СonditionsItemDetail(models.Model):
    category = models.ForeignKey(СonditionsItemCategory, related_name="details", on_delete=models.CASCADE, verbose_name="Пункт")
    title = models.CharField(max_length=200, verbose_name="Название подпункта")

    def __str__(self):
        return f"{self.category.name}: {self.title}"