# -*- coding: utf-8 -*-
from django.contrib import admin
from esporte_tec.membros.models import Colaborador
from esporte_tec.membros.models import OrgaoGoverno
from esporte_tec.membros.models import Academia
from esporte_tec.membros.models import Empresa


admin.site.register(Colaborador, admin.ModelAdmin)
admin.site.register(OrgaoGoverno, admin.ModelAdmin)
admin.site.register(Academia, admin.ModelAdmin)
admin.site.register(Empresa, admin.ModelAdmin)
