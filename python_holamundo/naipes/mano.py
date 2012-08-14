#encoding:utf-8
from mazo import Mazo

"""
	HERENCIA: Es la capacidad de definir una nueva clase que es una versión modificada de otra ya existente
		> Pros:
			- Se pueden agregar nuevos métodos a una clase sin modificar la clase existente
			- La nueva clase hereda todos los métodos de la clase existente
			- La clase existente se denomina clase padre y la nueva clase es llamada clase hija o subclase
			- La herencia puede facilitar la reutilización del código al permitir adaptar el comportamiento 
			  de la clase padre sin tener que modificarla.
			- A veces la estructura de la herencia refleja la estructura del problema, lo que facilita la 
			  lectura del código
		> Contras:
			- puede dificultar la lectura del programa: a veces no esta claro donde encontrar la definición
			  de un método
			- El código relevante puede estar diseminado por varios modulos
			- No siempre es necesaria, incluso en determinados problemas es mejor prescindir de herencia
			- Si la estructura del problema no nos guía hacia la herencia, dicho estilo de programación
			  puede hacer más mal que bien.
"""

# Mano hereda de Mazo
class Mano(Mazo):
	"""
	> __init__(): inicializa los atributos para la mano: nombre y cartas
		- nombre: identifica a esta mano, probablemente mediante el nombre del jugador que la sostiene
				  es opcional con un valor por omisión de cadena vacía.
		- cartas: es la lista de cartas de la mano, inicializada como lista vacía. 
	> eliminaCarta(): hereda de Mazo()
	> agregaCarta(): agrega cartas al mazo
		- append() agrega la nueva carta al final de la lista de cartas
	"""
	def __init__(self, nombre=""):
		self.cartas = []
		self.nombre = nombre

	def agregaCarta(self, carta):
		self.cartas.append(carta)






















