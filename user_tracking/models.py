from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserTracking(models.Model):
        user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_tracking')
        url = models.CharField(max_length=500)
        date = models.DateTimeField(auto_now_add=True)
