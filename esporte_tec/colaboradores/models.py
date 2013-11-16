# -*- coding: utf-8 -*-
from django.db import models



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
		return "%s - %s - %s" % (self.nome, self.email, self.area_interesse)


class OrgaoGoverno(models.Model):
	"""
	Model de cadastro de Governo
	"""

	razao_social = models.CharField("Razão Social", max_length=250)
	contato = models.CharField("Pessoa para contato", max_length=250)
	departamento = models.CharField("Departamento", max_length=250)
	email = models.EmailField("Email", max_length = 250)
	area_interesse = models.CharField("Área de interesse", max_length=250)
	telefone = models.CharField("Telefone", max_length=40)

	class Meta:
		verbose_name_plural = "Orgãos Governamentais"
		verbose_name = "Orgão Governamental"

	def __unicode__(self):
		return "%s - %s - %s - %s - %s - %s" % (self.razao_social, self.contato, self.departamento, self.email, self.area_interesse, self.telefone)


class Academia(models.Model):
	"""
	Model de cadastro de Academia
	"""

	razao_social = models.CharField("Razão Social", max_length=250)
	contato = models.CharField("Pessoa para contato", max_length=250)
	departamento = models.CharField("Departamento", max_length=250)
	email = models.EmailField("Email", max_length=250)
	telefone = models.CharField("Telefone", max_length=40)
	area_pesquisa = models.CharField("Área de pesquisa", max_length=250)
	area_interesse = models.CharField("Área de interesse", max_length=250)

	class Meta:
		verbose_name_plural = "Instituições Acadêmicas"
		verbose_name = "Instituição Acadêmica"

	def __unicode__(self):
		return "%s - %s - %s - %s - %s - %s - %s" % (self.razao_social, self.contato, self.departamento, self.email, self.telefone, self.area_pesquisa, self.area_interesse)




