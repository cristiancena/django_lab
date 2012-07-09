import os,sys
#encoding=utf-8

from django.db import models 			#clase con la descripcion del modelo
from django.contrib.auth.models import User	#Llama al modelo de usuario

# Create your models here.

class Bebida(models.Model):
	nombre		= models.CharField(max_length=50)
	ingredientes	= models.TextField()
	preparacion	= models.TextField()
	def __unicode__(self):
		return self.nombre

class Receta(models.Model):
			# dato cadena, longtud maxima 100 y unico
	titulo		= models.CharField(max_length=100,unique=True)
			# dato texto, con texto de ayuda
	ingredientes	= models.TextField(help_text='Redacta los ingredientes')
			# dato texto, con nombre: Preparacion
	preparacion	= models.TextField(verbose_name='Preparacion')
			# dato imagen, se almacenaran en la carpeta recetas, titulo: Imagen
	imagen 		= models.ImageField(upload_to='recetas',verbose_name='Imagen')
			# dato Fecha y Hora, almacena la fecha actual
	tiempo_registro = models.DateTimeField(auto_now=True)
			# Enlace al modelo Usuario que Django ya tiene construido
	usuario 	= models.ForeignKey(User)
	def __unicode__(self):
		return self.titulo

