from django import template

from main.models import Pyment

register = template.Library()

@register.simple_tag()
def tag_pyment():
    return Pyment.objects.all().first()