from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponse #importamos la clase HttpResponse perteneciente al modulo django.http
import datetime #importamos el modulo datetime de la biblioteca standard de python

#las funciones de vista deben tomar como primer argumento un objeto HttpRequest, 
#al que comunmente se le asigna el nombre request
def current_datetime(request):
	now  = datetime.datetime.now()
	#t = get_template('current_datetime.html')
	#html = t.render(Context({'current_date': now}))
	#return HttpResponse(html)
	return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request, offset):
	#offset es la cadena capturada por los parentesis en el patron URL
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	#html = "<html><body>In %s hour(s), it will be %s</body><html>" % (offset, dt)
	return render_to_response('hours_ahead.html',{'hour_offset':offset, 'next_time': dt})