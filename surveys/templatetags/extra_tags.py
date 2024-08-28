
from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    if value and arg:
        return round(value - arg, 2)
    else:
        return value

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')