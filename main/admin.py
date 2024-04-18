from django.contrib import admin
from .models import Slider, Advantage, Hit, New, About, Map, Contact, Pyment, Delivery
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

class AboutAdmin(forms.ModelForm):
    full_description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = About
        fields = '__all__'

class ContactAdmin(forms.ModelForm):
    full_description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Contact
        fields = '__all__'

class PymentAdmin(forms.ModelForm):
    full_description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Pyment
        fields = '__all__'

class DeliveryAdmin(forms.ModelForm):
    full_description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Delivery
        fields = '__all__'

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('caption', 'description', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)

@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('icon_class', 'text', )
    list_editable = ('text',)
    list_filter = ('text',)

@admin.register(Hit)
class HitAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('name', )
    

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'brief_description', )
    list_editable = ('brief_description',)
    fields = [
        "name",
        "slug",
        "brief_description",
        "full_description",
    ]
    form = AboutAdmin

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'brief_description', )
    list_editable = ('brief_description',)
    fields = [
        "name",
        "slug",
        "brief_description",
        "full_description",
    ]
    form = ContactAdmin

@admin.register(Pyment)
class PymentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'brief_description', )
    list_editable = ('brief_description',)
    fields = [
        "name",
        "slug",
        "brief_description",
        "full_description",
    ]
    form = PymentAdmin

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'brief_description', )
    list_editable = ('brief_description',)
    fields = [
        "name",
        "slug",
        "brief_description",
        "full_description",
    ]
    form = DeliveryAdmin

@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('title', 'iframe_url')
