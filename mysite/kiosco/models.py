#encoding=utf-8

from django.db import models

"""
class Config(models.Model):
	lenguaje		= select-options
	zona_horaria	= select-options
	moneda			= select-options
"""

class Moneda(models.Model):
	#ver carrito para mi profe de diseño
	nombre 				= models.CharField(max_length=30)
	iso 				= models.CharField(max_length=10)
	simbolo				= models.CharField(max_length=10)
	tasa_de_conversion 	= models.FloatField() 
	#moneda base = bool
	def __str__(self):
		return (str(self.simbolo) + " - " + str(self.nombre))

class Proveedor(models.Model):
	nombre 	= models.CharField(max_length = 30)
	#otrosDatos
	def __str__(self):
		return self.nombre

class Cliente(models.Model):
	nombre 				= models.CharField(max_length = 30)
	apellido			= models.CharField(max_length = 30)
	#email
	#telefono
	#avatar
	def __str__(self):
		return self.nombre

class Categoria(models.Model):
	nombre 	= models.CharField(max_length = 30)
	# esto debe ser recursivo, ni idea como hacer esto en python
	# 1 cat padre -> N cat hijas 
	def __str__(self):
		return self.nombre

class NombreProducto(models.Model):
	nombre 	= models.CharField(max_length = 30)
	def __str__(self):
		return self.nombre

class Etiqueta(models.Model):
	nombre 	= models.CharField(max_length = 30)
	def __str__(self):
		return self.nombre

class Marca(models.Model):
	nombre 	= models.CharField(max_length = 30)
	def __str__(self):
		return self.nombre

class TipoMedida(models.Model):
	tipo = models.CharField(max_length = 30)
	def __str__(self):
		return self.tipo

class Medida(models.Model):
	descripcion = models.CharField(max_length = 30)
	prefijo 	= models.CharField(max_length = 30)
	tipo 		= models.ForeignKey(TipoMedida)
	def __str__(self):
		return self.prefijo

class Impuesto(models.Model):
	"""
	tipo = {
		"porcentaje" : "%",
		"monto fijo" : "$"
	}
	tipo   		= models.CharField(max_length = 30)
	"""
	nombre 		= models.CharField(max_length = 30)
	valor  		= models.CharField(max_length = 30)
	def __str__(self):
		return self.nombre

class Descuento(models.Model):
	"""
	tipo = {
		"porcentaje" : "%",
		"monto fijo" : "$"
	}
	tipo   		= models.CharField(max_length = 30)
	"""
	nombre 		= models.CharField(max_length = 30)
	valor  		= models.CharField(max_length = 30)
	def __str__(self):
		return self.nombre

# EJEMPLO: Bombon Suizo Damevin x 250gr
# categoría: Bombon Suizo
# etiquetas: Bombones, Helados, Postres
# marca: Damevin
# nro: 250 
# medida: gr

class Producto(models.Model):
	nombre 				= models.ForeignKey(NombreProducto)
	categoria 			= models.ForeignKey(Categoria)		# recursivo
	etiquetas  			= models.ManyToManyField(Etiqueta) 	# no recursivo: keywords 
	marca 				= models.OneToOneField(Marca) 
	numero_medida 		= models.IntegerField()
	medida 				= models.OneToOneField(Medida) #tiene que quedar onda: "1.125 lts" nro + medida            	 
	stock 				= models.IntegerField()
	precio_de_costo 	= models.FloatField() #floatfield o permitir "tomar precio de una factura"
	impuestos 			= models.ManyToManyField(Impuesto)
	descuentos 			= models.ManyToManyField(Descuento)
	def __str__(self):
		return (str(self.nombre) + " " + str(self.marca) + " " + str(self.numero_medida) + " " + str(self.medida)) 
	def stock():
		return "devuelve el stock del producto"
		# stock = "cantidad de compras del producto (pedidos)" - "cantidad de ventas del producto (ventas)"
		# consultamos todos las compras
		# consultamos todas las ventas
		# compras - ventas

class Caja(models.Model):
	#caja o unidades: 1 caja -> N paquetes/unidades
	cantidad 			= models.IntegerField()
	def __str__(self):
		if str(self.cantidad) == "1":
			return "unidad/es"
		else:
			return ("caja de " + str(self.cantidad) + " unidades")

#lista de precio
#	- fernet branca x1 unidad de 1 litro 				= $50
# 	- fernet branca x1 caja de 6 unidades de 1 litro 	= $280

class ItemFactura(models.Model):
	producto 			= models.ForeignKey(Producto)
	nro_cantidad		= models.IntegerField()
	cantidad 			= models.OneToOneField(Caja)  
	# cantidad = producto * caja
	# stock > todas las cantidades de todas las compras menos las cantidades de todas las ventas
	precio 				= models.FloatField()
	def __str__(self):
		return (str(self.producto) + " " + str(self.nro_cantidad) + " " + str(self.cantidad))

# las facturas/pedidos guardan registro histórico de lo que se fue pagando y pueden actualizar 
# los precios de los productos mediante una sincronización con las listas de precio
# 

class Factura(models.Model):
	nro_factura			= models.IntegerField()
	proveedor 			= models.OneToOneField(Proveedor)
	fecha 				= models.DateField()
	items 				= models.ManyToManyField(ItemFactura)
	#total = suma de todos los items
	def __str__(self):
		return (str(self.proveedor) + " " + str(self.fecha))
	"""
	def costoPorCaja(self):      
		pass  
		# Producto.precio_costo ?
		# costo por cada unidad-paquete      
	def costoPorUnidad(self):       
		pass
		# costo por cada unidad-paquete      
	def costoPorMedida(self):            
		pass 
		# precio por litro o precio por kilo 
	def precioPorCaja(self):              
		pass 
		# costo por cada unidad-paquete      
	def precioPorUnidad(self):         
		pass 
		# costo por cada unidad-paquete      
	def precioPorMedida(self):                   
		pass 
		# precio por litro o precio por kilo
	"""

# cuando compramos determinados productos, de dicha compra o factura se actualizan las listas de precio
# dar opcion global de actualizacion automatica o no.
# una lista de precio debe poder 
# - dar precio a productos y cajas
# - a/desa/signar descuentos e impuestos
# - actualizar precios en masa por inflación

class ListaDePrecio(models.Model):
	# en frontend: permitir cargar precios para todos los productos existentes 
	# en la ultima factura o en alguna factura	
	nombre 				= models.CharField(max_length=30)
	moneda 				= models.ForeignKey(Moneda)
	productos 			= models.ManyToManyField(Producto) # validar que no se pueda cargar dos veces el mismo producto
	def __str__(self):
		return self.nombre
	# cuando consulto el precio de un producto 
	# éste estará sujeto a la última .
	# con cada actualizacion de la lista de precios va  
	def actualizaPrecio(self):
		pass
		# cuando en un nuevo pedido compramos un producto que tenemos en stock con precio viejo: calculamos
		# la diferencia y actualizamos el precio

# SALIDA DE MERCADERÍA
#==============================================================0

# un carrito es una posible orden, un posible pedido futuro 
class Carrito(models.Model):
	productos 	= models.ManyToManyField(Producto) 
	cliente 	= models.OneToOneField(Cliente)
	fecha 		= models.DateTimeField()
	def __str__(self):
		return (str(self.cliente) + " " + str(self.fecha))

class MedioDePago(models.Model):
	nombre 		= models.CharField(max_length = 30)
	comision 	= models.FloatField()
	def __str__(self):
		return str(self.nombre)

#los pedidos son onlines y pendientes de pago, cuando el pago se acredita se cierra la operación
class Pedido(models.Model):
	carrito 		= models.OneToOneField(Carrito)
	medio_de_pago 	= models.ForeignKey(MedioDePago)
	fecha 			= models.DateTimeField()
	def __str__(self):
		return (str(self.carrito) + " " + str(self.fecha))

# una venta fisica puede tener fiado, es decir:
# sale la mercadería pero no existe el pago
# si el pago no existe se asocia un fiado
# si el pago existe se cierra la operación
# acá va el lector de códigos de barras, el descuento de stock y la conexión con la registradora
class VentaFisica(models.Model):
	fecha 				= models.DateTimeField();
	productos			= models.ManyToManyField(Producto) 
	cliente 			= models.OneToOneField(Cliente) 			
	def __str__(self):
		return str(self.fecha)

# en los pagos: restar las ventas a ese cliente que no esten pagadas.
class PagoFisico(models.Model):
	cliente 			= models.OneToOneField(Cliente) 			
	monto 				= models.FloatField()
	def __str__(self):
		return str(self.cliente) + " - " + str(self.monto)



# COSTOS FIJOS
#==============================================================0

class Tarifa(models.Model):
	tarifa = models.CharField(max_length=30) 
	costo  = models.FloatField()
	def __str__(self):
		return self.tarifa

class Servicio(models.Model):
	servicio 	= models.CharField(max_length = 30)
	tarifa 		= models.FloatField()
	def __str__(self):
		return self.servicio

class ImpuestoAPagar(models.Model):
	impuesto 	= models.CharField(max_length = 30) 
	tarifa 		= models.ForeignKey(Tarifa)
	def __str__(self):
		return self.impuesto

class Empleado(models.Model):
	nombre 						= models.CharField(max_length=30)
	apellido					= models.CharField(max_length=30)
	precio_por_hora 			= models.ForeignKey(Tarifa)
	cantidad_de_horas_mensuales = models.FloatField()
	def __str__(self):
		return self.nombre
	def costo_mensual(self):
		pass #cantidad_de_horas_mensuales * precio_por_hora

class CostoFijo(models.Model):
	empleados = models.ForeignKey(Empleado)
	servicios = models.ForeignKey(Servicio)
	impuestos = models.ForeignKey(ImpuestoAPagar)
	def __str__(self):
		return self.id






