from django import template

register = template.Library()

@register.filter
def getList(d,val):
    return d.get(val)
