# -*- coding: utf-8 -*-
from django.db import models



class Colaborador(models.Model):

	"""
	Model responsável pelos Colaboradores
	"""

	nome = models.CharField("Nome", max_length=250)
	email = models.EmailField("Email", max_length=250)
	area_interesse = models.CharField("Área de interesse", max_length=250)
	
	class Meta:
		verbose_name_plural = "Colaboradores"

	def __unicode__(self):
		return "%s - %s - %s" % (self.nome, self.email, self.area_interesse)


class OrgaoGoverno(models.Model):
	"""
	Model de cadastro de Governo
	"""

	razao_social_governo = models.CharField("Razão Social", max_length=250)
	contato_governo = models.CharField("Pessoa para contato", max_length=250)
	departamento_governo = models.CharField("Departamento", max_length=250)
	email_governo = models.CharField("Email", max_length = 250)
	area_interesse_governo = models.CharField("Área de interesse", max_length=250)
	telefone_governo = models.CharField("Telefone", max_length=40)

	def __unicode__(self):
		return "%s - %s - %s - %s - %s - %s" % (self.razao_social_governo, self.contato_governo, self.departamento_governo, self.email_governo, self.area_interesse_governo, self.telefone_governo)

class Academia(models.Model):
	"""
	Model de cadastro de Academia
	"""

	razao_social_academia = models.CharField("Razão Social", max_length=250)
	contato_academia = models.CharField("Pessoa para contato", max_length=250)
	departamento_academia = models.CharField("Departamento", max_length=250)
	email_academia = models.CharField("Email", max_length=250)
	telefone_academia = models.CharField("Telefone", max_length=40)
	area_pesquisa = models.CharField("Área de pesquisa", max_length=250)
	area_interesse_academia = models.CharField("Área de interesse", max_length=250)

	def __unicode__(self):
		return "%s - %s - %s - %s - %s - %s - %s" % (self.razao_social_academia, self.contato_academia, self.departamento_academia, self.email_academia, self.telefone_academia, self.area_pesquisa, self.area_interesse_academia)

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

    class Meta:
    	verbose_name_plural = "Startups"

    def __unicode__(self):
        return "%s - %s - %s - %s - %s -%s - %s" % (self.razao_social, self.nome_fantasia, self.site, self.email, self.telefone, self.nome, self.pessoa_para_contato)


