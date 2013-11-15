# -*- coding: utf-8 -*-
from django.contrib import admin
from esporte_tec.colaboradores.models import Colaborador
from esporte_tec.colaboradores.models import Governo

admin.site.register(Colaborador, admin.ModelAdmin)
admin.site.register(Governo, admin.ModelAdmin)
