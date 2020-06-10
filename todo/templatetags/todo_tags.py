"""
DATE: https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#date
"""
import datetime
import time
import sys
from tkinter import *

from django import template

register = template.Library()


@register.simple_tag
def current_time(format_string):
    while True:
        from datetime import datetime
        now = datetime.now()
        sys.stdout.flush()
        time.sleep(1)
        return now
