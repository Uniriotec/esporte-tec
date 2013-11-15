# -*- coding: utf-8 -*-
from django.contrib import admin
from esporte_tec.colaboradores.models import Colaborador

admin.site.register(Colaborador, admin.ModelAdmin)
