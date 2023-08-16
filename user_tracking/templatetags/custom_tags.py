from django import template
from config import settings
register = template.Library()

@register.simple_tag
def ignore_tracking_check_url(url):
	if url in settings.URL_IGNORE_TRACKING:
		return 'not_checked'
	return 'checked'