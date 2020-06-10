from django import template
from django.contrib.auth.models import User

from accounts.models import UserProfile
from base.settings import COMPANY_NAME

register = template.Library()


@register.inclusion_tag('components/navbar_brand_link.html')
def navbar_brand_link(link):
    context = {
        'link': link,
        'title': COMPANY_NAME
    }
    return context


@register.simple_tag(name='user_badge')
def get_user_info():
    firstname = User.first_name
    lastname = User.last_name
    context = {
        'firstname': firstname,
        'lastname': lastname
    }
    return context
