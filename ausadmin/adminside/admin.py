# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import user,category,item

admin.site.register(category)
admin.site.register(item)
admin.site.register(user)
# Register your models here.
