# -*- coding: utf-8 -*-
from django.db import models

from model_utils import Choices



class Colaborador(models.Model):

    """
    Model responsável pelos Colaboradores
    """

    nome = models.CharField("Nome", max_length=250)
    email = models.EmailField("Email", max_length=250)
    area_interesse = models.ManyToManyField('areas.Area', verbose_name="Área de Interesse")


    class Meta:
        verbose_name_plural = "Colaboradores"

    def __unicode__(self):
        return "%s - %s" % (self.nome, self.email)


class OrgaoGoverno(models.Model):
    """
    Model de cadastro de Governo
    """

    razao_social = models.CharField("Razão Social", max_length=250)
    contato = models.CharField("Pessoa para contato", max_length=250)
    departamento = models.CharField("Departamento", max_length=250)
    email = models.EmailField("Email", max_length = 250)
    area_interesse = models.ManyToManyField('areas.Area', verbose_name="Área de Interesse")
    telefone = models.CharField("Telefone", max_length=40)

    class Meta:
        verbose_name_plural = "Instituições Governamentais"
        verbose_name = "Instituição Governamental"

    def __unicode__(self):
        return "%s - %s - %s - %s - %s" % (self.razao_social, self.contato, self.departamento, self.email, self.telefone)


class Academia(models.Model):
    """
    Model de cadastro de Instituições Acadêmicas
    """

    AREA_PESQUISA_CHOICES = Choices(
        (0, 'engenharia', 'engenharia'),
        (1, 'c_sociais', 'ciências sociais'),
        (2, 'c_saude', 'ciências da saúde'),
    )

    razao_social = models.CharField("Razão Social", max_length=250)
    contato = models.CharField("Pessoa para contato", max_length=250)
    departamento = models.CharField("Departamento", max_length=250)
    email = models.EmailField("Email", max_length=250)
    telefone = models.CharField("Telefone", max_length=40)
    area_interesse = models.ManyToManyField('areas.Area', verbose_name="Área de Interesse")

    area_pesquisa = models.IntegerField("Área de Pesquisa",choices=AREA_PESQUISA_CHOICES, default=AREA_PESQUISA_CHOICES.engenharia)

    class Meta:
        verbose_name_plural = "Instituições Acadêmicas"
        verbose_name = "Instituição Acadêmica"

    def __unicode__(self):
        return "%s - %s - %s - %s - %s" % (self.razao_social, self.contato, self.departamento, self.email, self.telefone)
