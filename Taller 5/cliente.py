import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:9000')
n1 = raw_input("ingrese el primer numero: ")
op = raw_input("ingrese el operador: (+,-,^,*,/,log, raiz) ")
n2 = raw_input("ingrese el segundo numero: ")
Op=n1+ '@' + op + '@' + n2
Op2=Op.split('@')
print "Resultado", s.operacion(Op2)

# Print list of available methods
#print s.system.listMethods()
#print s.system.methodHelp("div")