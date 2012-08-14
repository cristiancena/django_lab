#encoding:utf-8

from carta import Carta
from mazo import Mazo
from mano import Mano

# CARTAS ===============================================

carta1 = Carta(1, 11)
print carta1
# "Sota de Diamantes"

carta2 = Carta(1, 3)
print carta2
# "3 de Diamantes"

print carta2.listaDePalos[1]
# "Diamantes"

print carta1.__cmp__(carta2)
# 1

As = Carta(1,1)
print As
# "As de Diamantes"

Rey = Carta(1, 13)
print Rey
# "Rey de Diamantes"

print As.__cmp__(Rey) # -1 El As es menor que el Rey
print Rey.__cmp__(As) # 1  El Rey es mayor que el As

# MAZOS ===============================================

"""
mazo = Mazo()

mazo.eliminaCarta(As) #As de Diamantes
mazo.darCarta() # elimina el ultimo naipe de la lista, o sea, damos de abajo: Rey de Picas
print mazo

mazo.mezclar()
print mazo
"""

# MANOS ===============================================

























