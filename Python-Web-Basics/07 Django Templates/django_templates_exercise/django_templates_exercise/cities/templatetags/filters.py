from django import template

register = template.Library()


@register.filter(name='s_cities')
def s_cities(city_list):
    list_city = [c for c in city_list if c.city_name.startswith('S')]
    return list_city


@register.filter(name='p_cities')
def p_cities(city_list):
    list_city = [c for c in city_list if c.city_name.startswith('P')]
    return list_city
