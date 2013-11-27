from django.conf.urls import patterns, url

from esporte_tec.noticias import views

urlpatterns = patterns('',
    url(r'^noticias/$', views.ver_noticias, name='noticias'),
    url(r'^editais/$', views.ver_editais, name='editais'),
)


