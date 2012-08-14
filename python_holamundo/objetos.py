
#encoding:utf-8
from clases import Categoria, UnidadMedida, Marca, Producto, Cliente, Compra, Pago, FichaCliente

#===========================================#
hr = "="*50
print hr
#===========================================#
c0 = Categoria("gaseosas")
c1 = Categoria("gaseosas")
c2 = Categoria("cereales")
print "CATEGORIAS: " 
print c0
print c1 
print c2
print hr
#===========================================#
m0 = Marca("cocacola")
m1 = Marca("sprite")
m2 = Marca("trimacer")
print "MARCAS: "
print m0
print m1
print m2 
print hr
#===========================================#
um0 = UnidadMedida("1",4)
um1 = UnidadMedida("500",3)
um2 = UnidadMedida("1",1)
print "Unidades De Medida: "
print um0
print um1
print um2
print hr
#===========================================#
p0 = Producto("gaseosa cola", c0, m0, um0, 8, 30,   1)
p1 = Producto("gaseosa lima-limón", c1, m1, um1, 5, 30,   2)
p2 = Producto("arroz doble carolina", c2, m2, um2, 3.6, 35, 3)
print "PRODUCTOS: "
print p0, "precio final: " + str(p0.precio_final())
print p1, "precio final: " + str(p1.precio_final())
print p2, "precio final: " + str(p2.precio_final())
print hr
#===========================================#
c0 = Cliente("Anónimo","N-N")
c1 = Cliente("Juan","Gomez")
print "CLIENTES: "
print c0
print c1
print hr
#===========================================#
comp0 = Compra(c0, (p0.precio_final(), p1.precio_final()), "01/02/2012")
comp1 = Compra(c1, (p1.precio_final(), p2.precio_final()), "02/02/2012")
comp2 = Compra(c1, (p0.precio_final(), p1.precio_final(), p2.precio_final()), "03/02/2012")
print "COMPRAS: "
print comp0, comp0.total()
print comp1, comp1.total()
print comp2, comp2.total()
print hr
#===========================================#
pg0 = Pago(c1, 10)
print "PAGOS: "
print pg0
print hr
#===========================================#
fc0 = FichaCliente(c1,(comp1.total(),comp2.total()),(10,))
print "FICHA CLIENTE: "
print fc0, fc0.saldo()
print hr
