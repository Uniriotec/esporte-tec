from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

     url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
     url(r'^membros/$', TemplateView.as_view(template_name="membros.html"), name='membros'),
     url(r'^cadastro/$', TemplateView.as_view(template_name="cadastro.html"), name='cadastro'),
     url(r'^contato/$', TemplateView.as_view(template_name="contato.html"), name='contato'),
     url(r'^sobre/$', TemplateView.as_view(template_name="sobre.html"), name='sobre'),


     url(r'^', include('esporte_tec.noticias.urls')),
     url(r'^', include('esporte_tec.membros.urls')),
     
     
     # url(r'^noticias/$', TemplateView.as_view(template_name="noticias.html"), name='noticias'),
     #comentar essa url e mapear para a nova view(de editais) no urls da app noticias
     #url(r'^editais/$', TemplateView.as_view(template_name="editais.html"), name='editais'),
     #comentar essa url e mapear para a nova view(de politicas) no urls da app noticias
     url(r'^politicas/$', TemplateView.as_view(template_name="politicas.html"), name='politicas'),


     url(r'^admin/', include(admin.site.urls)),
)
