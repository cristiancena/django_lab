#encoding=utf-8

from django.db import models

# Cada marcador tiene una url
class Categoria(models.Model):
	nombre 			= models.CharField(max_length = 30)
	imagen 			= models.CharField(max_length = 30)
	def __str__(self):
		return self.nombre

class Etiqueta(models.Model):
	nombre 			= models.CharField(max_length = 30)
	def __str__(self):
		return self.nombre

class Clasificado(models.Model):
	nombre 			= models.CharField(max_length = 50)
	descripcion     = models.CharField(max_length = 50)
	tipo 			= models.CharField(max_length = 50) # producto, servicio
	precio 			= models.FloatField()
	def __str__(self):
		return str(self.nombre)

class Pagina(models.Model):
	imagen_portada 	= models.ImageField(upload_to='tmp')
	description     = models.CharField(max_length = 50)
	website 		= models.URLField()
	def __str__(self):
		return str(self.description)

# Los usuarios deben poder buscar por marca, por producto, por servicio, por anuncio 
class Marcador(models.Model):
	latitud 		= models.CharField(max_length = 30)
	longitud		= models.CharField(max_length = 30)
	nombre 			= models.CharField(max_length = 30)
	calle_nombre	= models.CharField(max_length = 50)
	calle_numero	= models.CharField(max_length = 50)
	categoria		= models.ForeignKey(Categoria)
	etiquetas		= models.CharField(max_length = 50)
	keywords 		= models.CharField(max_length = 50)
	clasificados	= models.ForeignKey(Clasificado)  
	pagina          = models.ForeignKey(Pagina)
	def __str__(self):
		return self.nombre

