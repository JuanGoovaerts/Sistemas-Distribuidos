import socket 
print "taller 2"
host="localhost"
puerto=9990
#operacion = "2@5".split("@")
#print operacion 
socket1= socket.socket()
socket1.connect((host,puerto))
operacion=raw_input("ingrese su instruccion separadas por @: ")
socket1.send(str(operacion))
#numero2=raw_input("ingrese otro numero: ")
#socket1.send(numero2)
operan=int(socket1.recv(1024))
print "puerto recibido :", operan
socket2 = socket.socket()
socket2.connect((host, operan))
socket2.send(str(operacion))
operan = socket2.recv(1024)
print "el  resultado de la operacion es : ", operan
tiempo= raw_input("presion enter para terminar")
socket1.close
