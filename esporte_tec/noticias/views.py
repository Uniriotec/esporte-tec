# -*- coding: utf-8 -*-
from annoying.decorators import render_to
from esporte_tec.noticias.models import Noticia
from esporte_tec.noticias.models import Edital

@render_to('noticias.html')
def ver_noticias(request):
    noticias = Noticia.objects.all()

    return {
        'noticias' : noticias,
    }


@render_to('editais.html')
def ver_editais(request):
    editais = Edital.objects.all()

    return {
        'editais' : editais,
    }