from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

     url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
     url(r'^membros/$', TemplateView.as_view(template_name="membros.html"), name='membros'),
     url(r'^contato/$', TemplateView.as_view(template_name="contato.html"), name='contato'),
     url(r'^noticias/$', TemplateView.as_view(template_name="noticias.html"), name='noticias'),
     url(r'^sobre/$', TemplateView.as_view(template_name="sobre.html"), name='sobre'),
    # Examples:
    # url(r'^$', 'esporte_tec.views.home', name='home'),
    # url(r'^esporte_tec/', include('esporte_tec.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
