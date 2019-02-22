from django import template

register = template.Library()

@register.filter(name='get_lifeform')
def get_lifeform(value, arg):
    return value.lifeform_set.filter(x=x, y=y).first();

@register.filter(name='y')
def y(value, arg):
    return value.filter(y=arg)

@register.filter(name='sub')
def sub(value, arg):
    try:
        value = int(value)
        arg = int(arg)
        if arg: return value - arg
    except: pass
    return ''

@register.filter(name='mul')
def mul(value, arg):
    try:
        value = int(value)
        arg = int(arg)
        if arg: return value * arg
    except: pass
    return ''
