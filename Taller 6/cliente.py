import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:9000')
n1 = raw_input("ingrese el primer numero: ")
op = raw_input("ingrese el operador: (+,-,^,*,/,log, raiz) ")
n2 = raw_input("ingrese el segundo numero: ")
Op=n1+ '@' + op + '@' + n2
s = xmlrpclib.ServerProxy('http://localhost:9000')
nombre = s.operacion(op)
s2 = xmlrpclib.ServerProxy(nombre)
print "Resultado", s2.op(n1, n2)

# Print list of available methods
#print s.system.listMethods()
#print s.system.methodHelp("div")