# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Profile(models.Model):
    """
    class containing projects' objects
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    profile_pic = models.ImageField( default = 'default.jpg',upload_to='profilepics/')
    bio = models.TextField(max_length=80, blank=True)
    contact = models.CharField(max_length =200,blank=True)
