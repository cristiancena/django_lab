#encoding:utf-8

from django.conf.urls import patterns, include, url

# esto ...
#from mysite.views import current_datetime, hours_ahead

# equivale a esto...
from mysite.views import * 
#con lo cual nos olvidamos la larga y tediosa declaración de importaciones de las vistas

from django.contrib import admin
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

#==============================================================
# vistas genericas de objetos: tomamos el modelo "Publishers" 

from django.views.generic import list_detail
from books.models import Publisher

publisher_info = {
    'queryset': Publisher.objects.all(),
    'template_name': 'books/publisher_list.html',
}

urlpatterns = patterns('',
    (r'^publishers/$', list_detail.object_list, publisher_info)
)

#==============================================================

urlpatterns += patterns('',
	# Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    url(r'^admin/doc/'  , include('django.contrib.admindocs.urls')),
    url(r'^admin/'      , include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^time/$', current_datetime),      
    url(r'^time/plus/(\d{1,2})/$', hours_ahead), 
)

urlpatterns += patterns('books.views',
    url(r'^$'                       ,'lista_libros', name='home'),
    url(r'^books/$'                 ,'lista_libros'),
    url(r'^books/search/$'          ,'search'),
    url(r'^contact/$'               ,'contact'),
    url(r'^books/add_publisher/$'   ,'add_publisher'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^debuginfo/$', 'mysite.views.debug'),       
    )

# '^' significa que requiere que el patron concuerde con el inicio de la cadena de caracteres
# '?' significa que exige que el patron concuerde con el fin de la cadena
# si iniciamos el patron con ^ y lo finalizamos con ? nos aseguramos que la (y solo la) url /time/ concuerde.  