from django.db import models
from django.contrib.auth.models import User

class UserProfile (models.Model):
    user = models.ForeignKey(User, related_name='profile')
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)


