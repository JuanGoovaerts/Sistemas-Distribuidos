import SocketServer
import socket
import math

host= "localhost"
puerto = 9990 
puerto1 = 9991
puerto2 = 9992
puerto3 = 9993
puerto4 = 9994
puerto5 = 9995
puerto6 = 9996
puerto7 = 9997

def op(ope):
	if ope  == "+":		
		return puerto1

	elif ope  == "-":
		return puerto2
	elif ope  == "*":
		return puerto3
	elif ope  == "/":
		return puerto4
	elif ope  == "p":
		return puerto5
	elif ope  == "r":
		return puerto6
	elif ope  == "l":		
		return puerto7

class mihandler(SocketServer.BaseRequestHandler):
	"""docstring for mihandler"""
	def handle(self):
		self.operacion = self.request.recv(1024).split("@")
		print self.operacion
		self.operan = str(op(self.operacion[2]))
		print self.operan
		self.request.send(self.operan)


def main():
	print "taller socket"
	server1= SocketServer.TCPServer((host, puerto), mihandler)
	print "server corriendo"
	server1.serve_forever()

main() 
		