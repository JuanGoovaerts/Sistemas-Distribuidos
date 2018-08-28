import socket 
print "taller 2"
host="localhost"
puerto=9989
#operacion = "2@5".split("@")
#print operacion 
socket1= socket.socket()
socket1.connect((host,puerto))
n1 = raw_input("ingrese el primer numero: ")
op = raw_input("ingrese el operador: (+,-,^,*,/,log,r) ")
n2 = raw_input("ingrese el segundo numero: ")
obj = n1+"@"+op+"@"+n2
socket1.send(obj)
#numero2=raw_input("ingrese otro numero: ")
#socket1.send(numero2)
operan=socket1.recv(1024)
print "el resultado de la operacion es: ", operan
tiempo= raw_input("presion enter para terminar")
socket1.close
