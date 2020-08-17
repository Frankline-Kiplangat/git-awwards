# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile, Projects, Events
# Register your models here.
admin.site.register(Projects)
admin.site.register(Events)
admin.site.register(Profile)
