import xmlrpclib

def operacion(number1, number2, operator):
	if operator  == "+":		
		return s.add(number1, number2)
	elif operator  == "-":
		return s.min(number1, number2)
	elif operator  == "^":
		return s.pow(number1, number2)
	elif operator  == "*":
		return s.mul(number1, number2)
	elif operator  == "/":
		return s.div(number1, number2)
	elif operator =="log":
		return s.log(number1, number2)
	elif operator =="raiz":
		return s.raiz(number1, number2)

s = xmlrpclib.ServerProxy('http://localhost:9000')
n1 = raw_input("ingrese el primer numero: ")
op = raw_input("ingrese el operador: (+,-,^,*,/,log) ")
n2 = raw_input("ingrese el segundo numero: ")

print operacion(int(n1), int(n2), op)

# Print list of available methods
print s.system.listMethods()
