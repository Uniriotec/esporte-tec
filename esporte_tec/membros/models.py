# -*- coding: utf-8 -*-
from django.db import models

from model_utils import Choices

class NomeOrRazaoMixing(object):

    def get_nome_or_razao(self):
        return self.razao_social

class Colaborador(models.Model, NomeOrRazaoMixing):
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

    def get_nome_or_razao(self):
        return self.nome


class OrgaoGoverno(models.Model, NomeOrRazaoMixing):
    """
    Model de cadastro de Governo
    """

    razao_social = models.CharField("Razão Social ou nome da Instituição", max_length=250)
    departamento = models.CharField("Departamento", max_length=250)
    contato = models.CharField("Pessoa para contato", max_length=250)
    email = models.EmailField("Email", max_length = 250)
    telefone = models.CharField("Telefone", max_length=40)
    area_interesse = models.ManyToManyField('areas.Area', verbose_name="Área de Interesse")


    class Meta:
        verbose_name_plural = "Instituições Governamentais"
        verbose_name = "Instituição Governamental"

    def __unicode__(self):
        return "%s - %s - %s - %s - %s" % (self.razao_social, self.departamento, self.contato, self.email, self.telefone)


class Academia(models.Model, NomeOrRazaoMixing):
    """
    Model de cadastro de Instituições Acadêmicas
    """

    AREA_PESQUISA_CHOICES = Choices(
        (0, 'engenharia', 'engenharia'),
        (1, 'c_sociais', 'ciências sociais'),
        (2, 'c_saude', 'ciências da saúde'),
    )

    razao_social = models.CharField("Razão Social ou Nome da Instituição", max_length=250)
    departamento = models.CharField("Departamento", max_length=250)
    site_departamento = models.CharField("Site do Departamento", max_length=250, blank=True)
    contato = models.CharField("Pessoa para contato", max_length=250)
    email = models.EmailField("Email", max_length=250)
    telefone = models.CharField("Telefone", max_length=40)
    area_interesse = models.ManyToManyField('areas.Area', verbose_name="Área de Interesse")
    area_pesquisa = models.IntegerField("Área de Pesquisa",choices=AREA_PESQUISA_CHOICES, default=AREA_PESQUISA_CHOICES.engenharia)
    resumo_projeto = models.CharField("Resumo do Projeto", max_length=250)

    class Meta:
        verbose_name_plural = "Instituições Acadêmicas"
        verbose_name = "Instituição Acadêmica"

    def __unicode__(self):
        return "%s - %s - %s - %s - %s - %s - %s" % (self.razao_social, self.departamento, self.site_departamento, self.contato, self.email, self.telefone, self.resumo_projeto)


class Empresa(models.Model, NomeOrRazaoMixing):
    """
    Model para o cadastro de Startups e Empresas
    """

    razao_social = models.CharField("Razão Social ou Nome Fantasia", max_length=250)
    site = models.CharField("Site", max_length=250, blank=True)
    pessoa_para_contato = models.CharField("Pessoa para contato",max_length=250)
    email = models.EmailField("Email", max_length=250)
    telefone = models.CharField("Telefone", max_length=40)

    area_interesse = models.ManyToManyField('areas.Area', verbose_name="Área de Interesse")
    is_startup = models.BooleanField("Marque aqui caso sua empresa seja uma start-up",default=False, blank=True)

    class Meta:
        verbose_name_plural = "Empresas"
        verbose_name = "Empresa"

    def __unicode__(self):
        return "%s - %s - %s - %s -%s" % (self.razao_social, self.site, self.pessoa_para_contato, self.email, self.telefone)
