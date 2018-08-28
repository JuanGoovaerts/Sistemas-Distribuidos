import SocketServer
import socket
import math

host= "localhost"
puerto = 9989 
puertosum= 9991
puertomin = 9992
puertodiv = 9993
puertopor = 9994
puertopow = 9995
puertoraiz = 9996
puertolog = 9997

def op(numero1, numero2, ope):
	socket1= socket.socket()
	puerto_op = puertosum
	if ope  == "+":		
		puerto_op = puertosum

	elif ope  == "-":
		puerto_op = puertomin
	elif ope  == "*":
		puerto_op = puertopor
	elif ope  == "/":
		puerto_op = puertodiv
	elif ope  == "^":
		puerto_op = puertopow
	elif ope  == "r":
		puerto_op = puertoraiz
	elif ope  == "log":		
		puerto_op = puertolog

	socket1.connect((host,puerto_op))
	socket1.send(numero1)
	print socket1.recv(1024)
	socket1.send(numero2)
	operan=socket1.recv(1024)
	return operan

class mihandler(SocketServer.BaseRequestHandler):
	"""docstring for mihandler"""
	def handle(self):
		self.operacion = self.request.recv(1024).split("@")
		print self.operacion
		self.numero1 = self.operacion[0]
		self.numero2 = self.operacion[2]
		self.operan = op(self.numero1, self.numero2, self.operacion[1])
		print "los numeros recibidos son: ", self.numero1, " y ",self.numero2, " y el resultado de la operacion es: ", self.operan
		self.request.send(self.operan)


def main():
	print "taller socket"
	
	

	server1= SocketServer.TCPServer((host, puerto), mihandler)
	print "server corriendo"
	server1.serve_forever()

main() 
		