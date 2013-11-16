# -*- coding: utf-8 -*-
from django.db import models

class Startup(models.Model):
    """
    Model para o cadastro de Startups
    Area inovação e com usted Arruda
    """

    razao_social = models.CharField("Razão Social", max_length=250)
    nome_fantasia = models.CharField("Nome fantasia", max_length=250)
    site = models.CharField("Site", max_length=250)
    email = models.EmailField("Email", max_length=250)
    telefone = models.CharField("Telefone", max_length=40)
    nome = models.CharField("Nome", max_length=40)
    pessoa_para_contato = models.CharField("Pessoa para contato",max_length=250)
    area_interesse = models.ManyToManyField('areas.Area', verbose_name="Área de Interesse")

    class Meta:
        verbose_name_plural = "Startups"
        verbose_name = "Startup"

    def __unicode__(self):
        return "%s - %s - %s - %s - %s -%s - %s" % (self.razao_social, self.nome_fantasia, self.site, self.email, self.telefone, self.nome, self.pessoa_para_contato)
