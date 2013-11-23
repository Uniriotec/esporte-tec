# -*- coding: utf-8 -*-
from django.contrib import admin
from esporte_tec.noticias.models import Noticia, Edital, PoliticaPublica

admin.site.register(Noticia, admin.ModelAdmin)
admin.site.register(Edital, admin.ModelAdmin)
admin.site.register(PoliticaPublica, admin.ModelAdmin)
