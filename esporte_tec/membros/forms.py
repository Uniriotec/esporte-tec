# -*- coding: utf-8 -*-
from django import forms

from esporte_tec.membros.models import Empresa

class EmpresaForm(forms.ModelForm):
    "Form do modelo de Empresa"

    class Meta:
        model = Empresa


