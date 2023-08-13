from django import template

register = template.Library()


@register.filter(name='multiply')
def multiply(val, arg):
    if type(val) == float:
        return round(val * arg, 2)
    else:
        return val * arg