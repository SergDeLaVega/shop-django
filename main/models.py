from django.db import models

# Create your models here.

class Slider(models.Model):
    photo = models.ImageField(upload_to='slides/')
    caption = models.TextField(blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        # Возвращает текст подписи в админ-панели
        return self.caption

    class Meta:
        verbose_name = 'слайд'
        verbose_name_plural = 'слайды'


class Advantage(models.Model):
    icon_class = models.CharField(max_length=100, help_text='Введите класс иконки Font Awesome')
    text = models.TextField(help_text='Введите текст преимущества')

    def __str__(self):
        return self.icon_class
    
    class Meta:
        verbose_name = 'Наши преимущества'
        verbose_name_plural = 'Наши преимущества'

class Hit(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название секции')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Самое покупаемое'
        verbose_name_plural = 'Самое покупаемое'

class New(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название секции')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Новинки'
        verbose_name_plural = 'Новинки'


class Map(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    iframe_url = models.URLField(verbose_name='Ссылка на iframe карты')

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    def __str__(self):
        return self.title

class About(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название страницы')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    brief_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название страницы')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    brief_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
    
class Pyment(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название страницы')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    brief_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплата'
    
class Delivery(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название страницы')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    brief_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставка'