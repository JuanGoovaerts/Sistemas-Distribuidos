import socket
import json
host = "localhost"
puerto = 9998
socket1 =  socket.socket()
socket1.connect((host,puerto))
n1 = raw_input("ingrese el primer numero: ")
op = raw_input("ingrese el operador: (+,-,^,*,/,log) ")
n2 = raw_input("ingrese el segundo numero: ")
obj = n1+"@"+op+"@"+n2
socket1.send(obj)
resultado = socket1.recv(1024)
print "el resultado de la operacion es "+resultado
tiempo= raw_input("presion enter para terminar")
socket.close()
