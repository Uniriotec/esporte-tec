# -*- coding: utf-8 -*-
from django import forms

from esporte_tec.membros.models import Empresa
from esporte_tec.membros.models import Colaborador
from esporte_tec.membros.models import Academia
from esporte_tec.membros.models import OrgaoGoverno

class EmpresaForm(forms.ModelForm):
    "Form do modelo de Empresa"

    class Meta:
        model = Empresa

class ColaboradorForm(forms.ModelForm):
	"Form do modelo de Colaborador"

	class Meta:
		model = Colaborador

class AcademiaForm(forms.ModelForm):
	"Form do modelo de Instituição Academica"

	class Meta:
		model = Academia

class GovernoForm(forms.ModelForm):
	"Form do modelo de Instituição Governamental"

	class Meta:
		model = OrgaoGoverno

