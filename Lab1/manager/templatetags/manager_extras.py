from django import template
from django.utils.html import format_html

from manager.constants import STATUS_CHOICES

register = template.Library()


@register.filter(is_safe=True)
def humanized(value):
    for status in STATUS_CHOICES:
        if value == status[0]:
            return format_html(status[1])
