# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import World

class WorldAdmin(admin.ModelAdmin):

    list_filter = ['name']
    search_fields = ['name']

admin.site.register(World)
