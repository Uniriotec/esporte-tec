from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from esporte_tec.membros import views

urlpatterns = patterns('',
    url(r'^cadastro_empresa/$', views.cadastrar_empresa, name='cadastro_empresa'),
    url(r'^sucesso/$', TemplateView.as_view(template_name="sucesso.html"), name='sucesso'),
)


