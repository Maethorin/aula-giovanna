from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^aula$', 'aula.views.home', name='home'),
    url(r'^calculadora/', include('calculadora.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
