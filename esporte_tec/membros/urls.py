from django.conf.urls import patterns, url

from esporte_tec.membros import views

urlpatterns = patterns('',
    url(r'^cadastro_empresa/$', views.cadastrar_empresa, name='cadastro_empresa'),
)


