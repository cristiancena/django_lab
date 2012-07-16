from django.http import HttpResponse #importamos la clase HttpResponse perteneciente al modulo django.http
import datetime #importamos el modulo datetime de la biblioteca standard de python

#las funciones de vista deben tomar como primer argumento un objeto HttpRequest, 
#al que comunmente se le asigna el nombre request
def current_datetime(request):
	now  = datetime.datetime.now()
	html = "<html><body><b>It is now</b> %s</body><html>" % now
	return HttpResponse(html)
