# -*- coding: utf-8 -*-
from django.contrib import admin
from esporte_tec.noticias.models import Noticia, Edital

admin.site.register(Noticia, admin.ModelAdmin)
admin.site.register(Edital, admin.ModelAdmin)
