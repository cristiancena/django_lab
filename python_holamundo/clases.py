#encoding:utf-8

#=======================================#
class Categoria:
	def __init__(self, categoria="categoria"):
		self.categoria = categoria		
	def __str__(self):
		return(self.categoria)
#=======================================#
class UnidadMedida:
	unidades = ("gr","kg","tn","cc","ltr")
	def __init__(self, numero=0, unidad="unidad"):
		self.numero = numero
		self.unidad = self.unidades[unidad]
	def __str__(self):
		return (str(self.numero) + str(self.unidad))
#=======================================#
class Marca:
	def __init__(self, marca="marca"):
		self.marca = marca
	def __str__(self):
		return (self.marca)
#=======================================#
class Producto:
	def __init__(self, nombre="nombre", categoria="categoria", marca="marca", medida="medida", precio_costo=0, marcado=0, cantidad=0):
		self.nombre				= nombre 
		self.categoria 			= categoria
		self.marca 				= marca
		self.medida 			= medida
		self.precio_costo 		= precio_costo
		self.marcado 			= marcado
		self.cantidad 			= cantidad
	def __str__(self): 
		return (str(self.categoria) + ", " + self.nombre + ", " + str(self.marca) + ", " + str(self.medida) + ", " + str(self.precio_costo) + ", " + str(self.marcado) + ", "+ str(self.cantidad))
	def precio_final(self):
		porcentaje   = float(self.precio_costo) * float(self.marcado) / float(100)
		precio_final = float(self.precio_costo) + porcentaje
		return precio_final
	def getCantidad():
		pass
	def setCantidad():
		pass
#=======================================#
class Cliente:
	def __init__(self, nombre="nombre", apellido="apellido"):
		self.nombre   = nombre
		self.apellido = apellido
	def __str__(self):
		return (self.nombre + " " + self.apellido)
#=======================================#
class Compra:
	def __init__(self, clientes="clientes", productos="productos", fecha="fecha"):
		self.fecha 		= fecha
		self.productos 	= productos
		self.clientes   = clientes
	def __str__(self):
		return (str(self.clientes) + ", " + str(self.productos) + ", " + self.fecha)
	def total(self):
		total = 0
		for producto in self.productos:
			total += producto
		return total
#=======================================#
class Pago:
	def __init__(self, cliente="cliente", monto="monto"):
		self.cliente = cliente
		self.monto = monto
	def __str__(self):
		return (str(self.cliente) + ", " + str(self.monto))
#=======================================#
class FichaCliente:
	def __init__(self, cliente="cliente", compras=0, pagos=0):
		self.cliente = cliente
		self.compras  = compras
		self.pagos = pagos
	def __str__(self):
		return (str(self.cliente) + ", " + str(self.compras) + " " + str(self.pagos))
	def saldo(self):
		total_compras = 0
		for compras in self.compras:
			total_compras += compras
		total_pagos = 0
		for pagos in self.pagos:
			total_pagos += pagos
		return total_pagos - total_compras

