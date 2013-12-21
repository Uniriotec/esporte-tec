# -*- coding: utf-8 -*-
from django import forms

from esporte_tec.membros.models import Empresa
from esporte_tec.membros.models import Colaborador
from esporte_tec.membros.models import Academia
from esporte_tec.membros.models import OrgaoGoverno

helper_selecionar_mais_opcoes = 'Para selecionar mais de uma opção, mantenha pressionada a tecla "Control" (ou "Command" se estiver utilizando um Mac).'

class EmpresaForm(forms.ModelForm):
    "Form do modelo de Empresa"

    def __init__(self, *args, **kwargs):
        super(EmpresaForm, self).__init__(*args, **kwargs)
        self.fields['area_interesse'].help_text = helper_selecionar_mais_opcoes

    class Meta:
        model = Empresa

class ColaboradorForm(forms.ModelForm):
    "Form do modelo de Colaborador"

    def __init__(self, *args, **kwargs):
        super(ColaboradorForm, self).__init__(*args, **kwargs)
        self.fields['area_interesse'].help_text = helper_selecionar_mais_opcoes

    class Meta:
        model = Colaborador

class AcademiaForm(forms.ModelForm):
    "Form do modelo de Instituição Academica"

    def __init__(self, *args, **kwargs):
        super(AcademiaForm, self).__init__(*args, **kwargs)
        self.fields['area_interesse'].help_text = helper_selecionar_mais_opcoes

    class Meta:
        model = Academia

class GovernoForm(forms.ModelForm):
    "Form do modelo de Instituição Governamental"

    def __init__(self, *args, **kwargs):
        super(GovernoForm, self).__init__(*args, **kwargs)
        self.fields['area_interesse'].help_text = helper_selecionar_mais_opcoes

    class Meta:
        model = OrgaoGoverno

