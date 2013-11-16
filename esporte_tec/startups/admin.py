# -*- coding: utf-8 -*-
from django.contrib import admin
from esporte_tec.startups.models import Startup

admin.site.register(Startup, admin.ModelAdmin)
