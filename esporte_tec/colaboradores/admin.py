# -*- coding: utf-8 -*-
from django.contrib import admin
from esporte_tec.colaboradores.models import Colaborador
from esporte_tec.colaboradores.models import OrgaoGoverno
from esporte_tec.colaboradores.models import Academia
from esporte_tec.colaboradores.models import Startup

admin.site.register(Colaborador, admin.ModelAdmin)
admin.site.register(OrgaoGoverno, admin.ModelAdmin)
admin.site.register(Academia, admin.ModelAdmin)
admin.site.register(Startup, admin.ModelAdmin)
