#encoding:utf-8

# asi debería ser mi arquitectura: from mysite.apps.books.models import Publisher
from books.models import Book
from books.models import Publisher

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.core.mail import send_mail
from django.db.models import Q
from forms import ContactForm

from forms import addBooksPublisher

#================================================

def lista_libros(request):
	books = Book.objects.all()
	if request.user.is_authenticated():
		usuario = "Hola " + str(request.user.username)
	else:
		usuario = "es anonimo"
	return render_to_response('books/books.html',{'lista':books, 'usuario':usuario}, context_instance=RequestContext(request))

#================================================

def search(request):
	query = request.GET.get('q','') #busca el parametro 'q' que viene via get | retorna un string vacio si el parametro no fue suministrado
	if query:
		#los objetos Q se usan para contruir consultas
		#icontains es una busqueda en la que no se distinguen mayusculas de minusculas, internamente usa el operador LIKE de SQL
		#distinct elimina los duplicados
		qset = (
			Q(title__icontains=query) | 
			Q(authors__first_name__icontains=query) |
			Q(authors__last_name__icontains=query)
		)
		results = Book.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("books/search.html",{
		"results": results,
		"query": query
	})

#================================================

def contact(request):
    info_enviado = False # todavia no se envio
    asunto  = ""
    correo  = ""
    mensaje = ""
    if request.method == 'POST':
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            info_enviado = True 
            asunto  = formulario.cleaned_data['subject']
            correo  = formulario.cleaned_data['email']
            mensaje = formulario.cleaned_data['message']
            """cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')"""
    else:
        formulario = ContactForm(
            initial={'subject': 'placeholder para subject!'}
        )
    ctx = {'form':formulario, 'info_enviado':info_enviado, 'asunto':asunto, 'correo':correo, 'mensaje':mensaje}  
    return render_to_response('books/contact_form.html', ctx, context_instance=RequestContext(request))

#================================================
#formularios que aprovechan los modelos (DRY) <- no llegue a esto todavía

def add_publisher(request):
	if request.method == 'POST':
		form = addBooksPublisher(request.POST)
		info = "Inicializando"
		if form.is_valid():
			# si es valido obtenemos los datos
			name 			= form.cleaned_data['name']
			address			= form.cleaned_data['address']
			city 			= form.cleaned_data['city']
			state_province 	= form.cleaned_data['state_province']
			country 		= form.cleaned_data['country']
			website 		= form.cleaned_data['website'] 
			p = Publisher()
			p.name 			= name
			p.address		= address
			p.city 			= city
			p.state_province= state_province
			p.country 		= country
			p.website 		= website
			p.save() #guarda el objeto
			#return HttpResponseRedirect('/add_publisher/thanks/')
			info = "se guardó satisfactoriamente!"
		else:
			info = "información con datos incorrectos"
		form = addBooksPublisher()
		ctx  = {'form':form, 'informacion':info}  
		return render_to_response('books/add_publisher.html', ctx, context_instance=RequestContext(request)) 
	else: #GET
		form = addBooksPublisher()
		ctx  = {'form':form}  
		return render_to_response('books/add_publisher.html', ctx, context_instance=RequestContext(request))


























