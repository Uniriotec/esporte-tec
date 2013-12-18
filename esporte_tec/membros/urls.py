from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from esporte_tec.membros import views

urlpatterns = patterns('',
    url(r'^cadastro_empresa/$', views.cadastrar_empresa, name='cadastro_empresa'),
    url(r'^cadastro_colaborador/$', views.cadastrar_colaborador, name='cadastro_colaborador'),
    url(r'^cadastro_academia/$', views.cadastrar_instituicao_academica, name='cadastro_academia'),
    url(r'^cadastro_governo/$', views.cadastrar_instituicao_governamental, name='cadastro_governo'),
    #url(r'^colaborador/$', views.exibir_informacoes_colaborador, name='colaborador'),
    url(r'^sucesso/$', TemplateView.as_view(template_name="sucesso.html"), name='sucesso'),
)


