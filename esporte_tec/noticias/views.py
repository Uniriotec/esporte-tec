# -*- coding: utf-8 -*-
from annoying.decorators import render_to
from esporte_tec.noticias.models import Noticia

@render_to('noticias.html')
def ver_noticias(request):
    noticias = Noticia.objects.all()

    return {
        'noticias' : noticias,
    }
