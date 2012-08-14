#encoding=utf-8

from django.contrib import admin
from turismo.models import Categoria, Etiqueta, Marcador, Pagina, Clasificado

admin.site.register(Categoria)
admin.site.register(Etiqueta)
admin.site.register(Marcador)
admin.site.register(Pagina)
admin.site.register(Clasificado)

"""
diferencia entre pagina, sitio y aplicacion
que es: un buscador de entidades y avisos clasificados basado en mapas
para que sirve en general: para orientar a turistas y ciudadanos en la búsqueda de entidades y ofertas.
para que le sirve al usuario: para brindar información turística, localizar entidades y encontrar ofertas
para que le sirve al miembro: para exhibir su oferta.
para que le sirve al padrino: como herramienta premio/castigo, para afianzar, fidelizar y atraer comercios, como plataforma publicitaria y de propaganda política.


licencia 1 $1000xmes : derechos sobre la identidad corporativa: dominio, marca, colores de gestión.
licencia 2 $1000xmes : derechos sobre la publicidad global: banners. fuera del mapa. 
licencia 3 $1000xmes : derechos sobre la publicidad de los marcadores. Dentro del mapa 

el padrino nunca tendra derecho sobre:
las decisiones sobre diseño estructurales, el layout, la tipografía, 
las decisiones sobre accesibilidad y estandares y normativas w3c en general
las decisiones sobre arquitectura de la información, modelo de datos, lógica de programación y el software en general.
las libertades individuales sobre el contenido generado por los usuarios,
no tendrá acceso a la información sensible y privada de los usuarios ni podrá usarla para ningún fin.

calcular porcentaje:
valor + (valor/float(1.porcentaje))
"""