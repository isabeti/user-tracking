from django import template
from django.urls import reverse_lazy

register = template.Library()


@register.simple_tag
def is_active_home_sidebar(request, app_name, url_name):
    if request.path == reverse_lazy(f'{app_name}:{url_name}'):
        return 'active'
    return 'not_active'

@register.simple_tag
def is_active_visotor_sidebar(request, app_name, url_name):
    if request.path == reverse_lazy(f'{app_name}:{url_name}'):
        return 'active'
    return 'not_active'

@register.simple_tag
def is_active_logged_sidebar(request, app_name, url_name):
    if request.path == reverse_lazy(f'{app_name}:{url_name}'):
        return 'active'
    return 'not_active'

@register.simple_tag
def is_active_registered_sidebar(request, app_name, url_name):
    if request.path == reverse_lazy(f'{app_name}:{url_name}'):
        return 'active'
    return 'not_active'

@register.simple_tag
def is_active_settings(request, app_name, url_name):
    if request.path == reverse_lazy(f'{app_name}:{url_name}'):
        return 'active'
    return 'not_active'