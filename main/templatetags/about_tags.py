from django import template

from main.models import About

register = template.Library()

@register.simple_tag()
def tag_about():
    return About.objects.all().first()
