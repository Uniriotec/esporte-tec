# -*- coding: utf-8 -*-
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

class Area(MPTTModel):
    """
    Uma área, usado para categorização de dados.
    """

    nome = models.CharField("Nome", max_length=250, blank=False, null=False)
    parent = TreeForeignKey('self',related_name="children",null=True,blank=True, verbose_name="Área Pai")

    class Meta:
        verbose_name_plural = "áreas"
        verbose_name = "área"

    class MPTTMeta:
        order_insertion_by = ['nome']

    def nome_completo(self):
        "retorna o nome completo de uma área, isso é, junto com todos os seus pais"

        nome_completo = self.nome
        for pai in self.get_ancestors(ascending=True, include_self=False):
            nome_completo = pai.nome + "/" + nome_completo

        return nome_completo


    def __unicode__(self):

        return self.nome_completo()
