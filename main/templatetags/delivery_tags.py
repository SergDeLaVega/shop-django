from django import template

from main.models import Delivery

register = template.Library()

@register.simple_tag()
def tag_delivery():
    return Delivery.objects.all().first()
