# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class AbsLink(models.Model):
    """
    Classe abstrata que possui dados genericos de uma referencia para um link
    Por ser abstrata não é salva no BD, é so para facilitar a utilização
    de OO
    """

    link = models.URLField("Link",max_length=250, blank=True, null=True)
    titulo = models.CharField("Título", max_length=250, blank=False, null=False)
    descricao = models.TextField("Descrição")
    data_publicacao = models.DateTimeField("Data de Publicação", default=timezone.now)

    class Meta:
        abstract = True


class Noticia(AbsLink):
    """
    Representa um link para uma noticia noticia no sistema
    Herda de AbsLink
    """
    class Meta:
        verbose_name_plural = "notícias"

    def __unicode__(self):
        return self.titulo


class Edital(AbsLink):
    """
    Representa um link para um edital no sistema
    Herda de AbsLink
    """

    orgao_governo = models.ForeignKey(
            'colaboradores.OrgaoGoverno',
            related_name='editais',
            verbose_name="Orgão do Governo"
    )

    class Meta:
        verbose_name_plural = "editais"

    def __unicode__(self):
        return self.titulo

class PoliticaPublica(AbsLink):
    """
    Representa um link para uma Politica Publica no sistema
    Herda de AbsLink
    """

    class Meta:
        verbose_name_plural = "políticas públicas"
        verbose_name = "política pública"

    def __unicode__(self):
        return self.titulo
