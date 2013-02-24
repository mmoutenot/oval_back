from django.db import models
from user_profile.models import UserProfile

class Group(models.Model):
    name  = models.CharField(max_length=120)
    users = models.ManyToManyField(UserProfile)

class Tag(models.Model):
    name  = models.CharField(max_length=40)

class Post (models.Model):
    kind  = models.CharField(max_length = 30)
    url   = models.URLField(max_length = 400)
    date  = models.DateTimeField(auto_now_add = True)
    group = models.ForeignKey(Group)
    user  = models.ForeignKey(UserProfile)
    tags  = models.ManyToManyField(Tag)

