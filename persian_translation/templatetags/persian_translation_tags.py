from django import template

register = template.Library()


@register.filter
def translate_number(number):
    number = str(number)
    english_to_persian_table = number.maketrans('0123456789', '۰١٢٣٤٥٦٧٨٩')
    return number.translate(english_to_persian_table)
