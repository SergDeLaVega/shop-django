from django import template

from main.models import Contact

register = template.Library()

@register.simple_tag()
def tag_contact():
    return Contact.objects.all().first()
