import datetime

from django import template

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.today().strftime(format_string)