from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name  = models.CharField(max_length=120)
    users = models.ManyToManyField(User)

class Tag(models.Model):
    name  = models.CharField(max_length=40)

class Post (models.Model):
    kind  = models.CharField(max_length = 30)
    url   = models.URLField(max_length = 400)
    date  = models.DateTimeField(auto_now_add = True)
    group = models.ForeignKey(Group)
    user  = models.ForeignKey(User)
    tags  = models.ManyToManyField(Tag)


from django.contrib import admin
admin.site.register(Group)
admin.site.register(Tag)
admin.site.register(Post)

