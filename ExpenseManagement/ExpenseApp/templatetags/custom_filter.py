from django import template

register = template.Library()
from ..models import *

@register.filter(name='TOTAL_PRICE')
def TOTAL_PRICE(price,quantity):
    return price*quantity
    