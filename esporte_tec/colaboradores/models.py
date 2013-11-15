# -*- coding: utf-8 -*-
from django.db import models

class Colaborador(models.Model):

	"""
	Model responsável pelos Colaboradores
	"""

	nome_colaborador = models.CharField("Nome", max_length=250)
	email_colaborador = models.CharField("Email", max_length=250)
	area_interesse = models.CharField("Área de interesse", max_length=250)


	def __unicode__(self):
		return "%s - %s - %s" % (self.nome_colaborador, self.email_colaborador, self.area_interesse)


class Governo(models.Model):
	"""
	Model de cadastro de Governo
	"""

	razao_social_governo = models.CharField("Razão Social", max_length=250)
	contato_governo = models.CharField("Pessoa para contato", max_length=250)
	departamento_governo = models.CharField("Departamento", max_length=250)
	email_governo = models.CharField("Email", max_length = 250)
	area_interesse_governo = models.CharField("Área de interesse", max_length=250)
	telefone_governo = models.CharField("Telefone", max_length=20)

	def __unicode__(self):
		return "%s - %s - %s - %s - %s - %s" % (self.razao_social_governo, self.contato_governo, self.departamento_governo, self.email_governo, self.area_interesse_governo, self.telefone_governo)

