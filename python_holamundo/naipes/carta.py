#encoding:utf-8

class Carta:
	"""
	Documentación de la clase Carta:
		> Codificamos los valores y palos con números enteros
			- Palos:
				- Treboles	-> 0
				- Diamantes	-> 1
				- Corazones	-> 2
				- Picas		-> 3
			- Valores:
				- nada 		-> 0
				- As 		-> 1
				- 2 		-> 2
				... 		-> ...
				- 10 		-> 10
				- Sota 		-> 11
				- Reina 	-> 12
				- Rey 		-> 13
			- Ej: 
				- self.listaDePalos[self.palo] se traduce:
				Usa el atributo palo del objeto self como un índice dentro del atributo de clase denominado
				listaDePalos y selecciona la cadena correspondiente. 
		> __init__() (constructor?): Toma un parámetro opcional para cada atributo.
		> Comparación:
			- Para los tipos definidos por el usuario, podemos sustituir el comportamiento de los operadores
			internos si proporcionamos un método llamado __cmp__(). 
	"""
	
	listaDePalos   = ["Tréboles", "Diamantes", "Corazones", "Picas"]
	listaDeValores = ["nada", "As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Sota", "Reina", "Rey"]
	
	def __init__(self, palo=0, valor=0):
		self.palo  = palo
		self.valor = valor
	
	def __str__(self):
		return (self.listaDeValores[self.valor] + " de " + self.listaDePalos[self.palo])	

	def __cmp__(self, otro):
		# controlar el palo
		if self.palo > otro.palo: return 1
		if self.palo < otro.palo: return -1
		# si son del mismo palo
		if self.valor > otro.valor: return 1
		if self.valor < otro.valor: return -1
		# los valores son igualos, es un empate
		return 0































