from django import template

register = template.Library()


@register.simple_tag
def populations(city_data):
    output = ', '.join(f"{c.id}-{c.city_population}" for c in city_data)
    return output
