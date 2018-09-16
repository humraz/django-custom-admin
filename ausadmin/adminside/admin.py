# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import user,category,item,booking

admin.site.register(category)
admin.site.register(item)
admin.site.register(user)
admin.site.register(booking)

# Register your models here.
