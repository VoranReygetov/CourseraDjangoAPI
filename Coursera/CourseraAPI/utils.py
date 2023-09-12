# utils.py
# from decimal import Decimal
import bleach

# def calculate_discount(product):
#     return round(product.price * Decimal(0.8), ndigits=2)

def bleachvalidate(attrs, *args):
    for items in args:
        attrs[items] = bleach.clean(attrs[items])