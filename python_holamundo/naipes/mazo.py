#encoding:utf-8
from carta import Carta

class Mazo:
	"""
		Documentación de la clase Mazo:
		> Barajar el mazo:
			- Del modulo random usamos randrange() que toma dos enteros como argumentos y elige
			un numero entero de forma aleatoria en el rango a <= x <b
	"""
	
	def __init__(self):
		self.cartas = []
		for palo in range(4):
			for valor in range(1, 14):
				self.cartas.append(Carta(palo, valor))
	
	def __str__(self):
		# usamos la variable s como acumulador
		s = ""
		for i in range(len(self.cartas)):
			# *1 proporciona una cantidad de espacios igual al valor actual de i
			s = s + " "*i + str(self.cartas[i]) + "\n" 
		return s
	
	def mezclar(self):
		import random
		nCartas = len(self.cartas)
		for i in range(nCartas):
			j = random.randrange(i, nCartas) # para cada naipe del mazo seleccionamos un naipe al azar entre aquellos que no han sido intercambiados aún.
			# intercambiamos el naipe actual (i) con el naipe seleccionado (j)
			self.cartas[i], self.cartas[j] =\
				self.cartas[j], self.cartas[i]
	
	def eliminaCarta(self, carta):
		"""
		>INFO: 
			- in retorna true si el 1er operando (carta) está en el 2do operando (self.cartas (lista o tupla))
			si el 1er operando es un objeto, Python usa el método __cmp__ del objeto para determinar la
			igualdad entre los elementos de la lista.

		>DOCUMENTACION:
			- Toma un naipe como parámetro
			- Si el naipe se encuentra en el mazo:
				- Lo elimina y retorna verdadero
			- Sino:
				- Retorna falso
		"""
		if carta in self.cartas:
			self.cartas.remove(carta)
			return 1
		else:
			return 0

	def darCarta(self):
		"""
		> pop() elimina el ultimo naipe en la lista, por tanto: 
			- Estamos repartiendo desde el extremo inferior del mazo

		"""
		return self.cartas.pop()

	def estaVacio(self):
		""" Devuelve verdadero si el mazo no contiene ningún naipe"""
		return (len(self.cartas) == 0)

	def repartir(self, manos, nCartas=999):
		nManos = len(manos)
		for i in range(nCartas):
			if self.estaVacio(): break 	# fin si se acaban las cartas
			carta = self.darCarta() 	# da la carta superior
			mano  = manos[i % nManos] 	# a quien le toca?
			mano.agregaCarta(carta) 	# agrega la carta a la mano































