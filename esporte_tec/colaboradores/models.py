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

