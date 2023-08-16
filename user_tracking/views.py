from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserTracking
from datetime import timedelta, datetime
from django.db.models import Q
import pandas as pd
from config import settings
from config import urls
# Create your views here.

def get_url_apps():
	url_apps = []
	for i in urls.urlpatterns:
		str_index = str(i)
		lst_index = str_index.split(' ')
		url_apps.append(lst_index[-1][1:-2])
	return url_apps

def home(request):
	context = {
		'objects': UserTracking.objects.all(),
		'visitors_count': UserTracking.objects.all().count(),
		'logins_count': User.objects.filter(last_login__date=datetime.today()).count(),
		'Registrants_count': User.objects.filter(date_joined__date=datetime.today(), is_active=True).count(),


		"visitors_labels": [datetime.today()],
		"visitors_values": [UserTracking.objects.all().count()],

		"logins_labels": [datetime.today()],
		"logins_values": [User.objects.filter(last_login__date=datetime.today()).count()],

		"Registrants_labels": [datetime.today()],
		"Registrants_values": [User.objects.filter(date_joined__date=datetime.today(), is_active=True).count()],

	}
	return render(request, 'user_tracking/home.html', context)

def visitors(request):
	context = {
		'objects': UserTracking.objects.filter(date__date=datetime.today()),

		"labels": [datetime.today()],
		"values": [UserTracking.objects.filter(date__date=datetime.today()).count()],
	}
	return render(request, 'user_tracking/visitors.html', context)

def visitors_filter(request):
	if request.method == 'POST':
		start_date = request.POST.get('start_date')
		end_date = request.POST.get('end_date')

		chart_labels = pd.date_range(start=start_date,end=end_date)
		chart_values = []

		for i in chart_labels:
			count_objects = UserTracking.objects.filter(date__date=i).count()
			chart_values.append(count_objects)

		context = {
			'objects': UserTracking.objects.filter(Q(date__date__gte=start_date) & Q(date__date__lte=end_date)),

			"labels": chart_labels,
			"values": chart_values,
		}
		return render(request, 'user_tracking/filter/visitors_filter.html', context)


def users_logged(request):
	context = {
		'e_date': datetime.today(),
		'objects': User.objects.filter(last_login__date=datetime.today()),

		"labels": [datetime.today()],
		"values": [User.objects.filter(last_login__date=datetime.today()).count()],
	}
	return render(request, 'user_tracking/users_logged.html', context)

def users_logged_filter(request):
	if request.method == 'POST':
		start_date = request.POST.get('start_date')
		end_date = request.POST.get('end_date')

		chart_labels = pd.date_range(start=start_date,end=end_date)
		chart_values = []

		for i in chart_labels:
			count_objects = User.objects.filter(last_login__date=i).count()
			chart_values.append(count_objects)

		context = {
			'objects': User.objects.filter(Q(last_login__date__gte=start_date) & Q(last_login__date__lte=end_date)),

			"labels": chart_labels,
			"values": chart_values,
		}
		return render(request, 'user_tracking/filter/users_logged_filter.html', context)



def users_registered(request):
	context = {
		'objects': User.objects.filter(date_joined__date=datetime.today(), is_active=True),

		"labels": [datetime.today()],
		"values": [User.objects.filter(date_joined__date=datetime.today(), is_active=True).count()],
	}
	return render(request, 'user_tracking/users_registered.html', context) 

def users_registered_filter(request):
	if request.method == 'POST':
		start_date = request.POST.get('start_date')
		end_date = request.POST.get('end_date')

		chart_labels = pd.date_range(start=start_date,end=end_date)
		chart_values = []

		for i in chart_labels:
			count_objects = User.objects.filter(date_joined__date=i).count()
			chart_values.append(count_objects)

		context = {
			'objects': User.objects.filter(Q(date_joined__date__gte=start_date) & Q(date_joined__date__lte=end_date)),

			"labels": chart_labels,
			"values": chart_values,
		}
		return render(request, 'user_tracking/filter/users_registered_filter.html', context) 

def ignore_tracking(request):
	if request.method == 'GET':
		context = {
			'urls': get_url_apps(),
		}
		return render(request, 'user_tracking/ignore_tracking.html', context)

	elif request.method == 'POST':
		url_apps = get_url_apps()

		ignore_tracking_lst = []
		for i in url_apps:
			args = request.POST.get(i)
			if args != 'on':
				ignore_tracking_lst.append(i)
		settings.URL_IGNORE_TRACKING = ignore_tracking_lst
		return redirect('user_tracking:ignore_tracking')