from django import template

register = template.Library()


@register.filter(is_safe=True)
def is_numeric(value):
    return "{}".format(value).isdigit()


tilraun = is_numeric('ys1bo59k1bgy8sqettxl0cu9hhf1lh58')
print(tilraun)