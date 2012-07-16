from django.conf.urls import patterns, include, url
from mysite.views import current_datetime

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^time/$', current_datetime)
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

# '^' significa que requiere que el patron concuerde con el inicio de la cadena de caracteres
# '?' significa que exige que el patron concuerde con el din de la cadena
# si iniciamos el patron con ^ y lo finalizamos con ? nos aseguramos que la (y solo la) url /time/ concuerde.  