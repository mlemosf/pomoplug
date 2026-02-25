from datetime import timedelta

from django import template

register = template.Library()


@register.filter
def seconds_to_hhmm(seconds):
    if not seconds:
        return "00:00"
    return str(timedelta(seconds=seconds))[2:]
