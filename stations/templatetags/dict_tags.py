from django import template

register = template.Library()


@register.filter(name='get')
def get(dict: dict, key):
    return dict[key]