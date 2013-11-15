# -*- coding: utf-8 -*-
from django.contrib import admin
from esporte_tec.colaboradores.models import Colaborador
from esporte_tec.colaboradores.models import Governo
from esporte_tec.colaboradores.models import Academia

admin.site.register(Colaborador, admin.ModelAdmin)
admin.site.register(Governo, admin.ModelAdmin)
admin.site.register(Academia, admin.ModelAdmin)
