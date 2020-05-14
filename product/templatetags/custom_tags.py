from django import template

register = template.Library()


@register.filter(is_safe=True)
@register.inclusion_tag('base.html')
def is_numeric(value):
    return "{}".format(value).isdigit()


