from django.urls import path
from .views import *

app_name = 'user_tracking'
urlpatterns = [
	path('', home, name='home'),
	path('visitors/', visitors, name='visitors'),
	path('users/logged/', users_logged, name='users_logged'),
	path('users/registered/', users_registered, name='users_registered'),

	path('users/logged/filter/', users_logged_filter, name='users_logged_filter'),
	path('users/registered/filter/', users_registered_filter, name='users_registered_filter'),
	path('visitors/filter/', visitors_filter, name='visitors_filter'),

	path('ignore/tracking/', ignore_tracking, name='ignore_tracking')

]

