import SocketServer
import math

def op(numero1, numero2):
	return numero1 / numero2

class mihandler(SocketServer.BaseRequestHandler):
	"""docstring for mihandler"""
	def handle(self):		
		self.numero1 = int(self.request.recv(1024))
		self.request.send("pase")
		self.numero2 = int(self.request.recv(1024))
		self.operan = str(op(self.numero1, self.numero2))
		print "los numeros recibidos son: ", self.numero1, " y ",self.numero2, " y el resultado de la operacion es: ", self.operan
		self.request.send(self.operan)

def main():
	host= "localhost"
	puerto = 9993

	server1= SocketServer.TCPServer((host, puerto), mihandler)
	print "server1 corriendo"
	server1.serve_forever()

main() 