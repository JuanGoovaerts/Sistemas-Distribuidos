import SocketServer
from math import log
def operacion(number1, number2, operator):
	if operator  == "+":		
		return number1 + number2
	elif operator  == "-":
		return number1 - number2
	elif operator  == "^":
		return pow(number1, number2)
	elif operator  == "*":
		return number1 * number2
	elif operator  == "/":
		return number1 / number2
	elif operator =="log":
		return log(number1, number2)

class mihandler(SocketServer.BaseRequestHandler):
	def handle(self):
		valores = self.request.recv(1024).split("@")
		print valores
		n1 = int(valores[0])
		op = str(valores[1])
		n2 = int(valores[2])
		respuesta = str(operacion(n1,n2,op))
		self.request.send(respuesta)

def main():
	print "taller socket 1"
	host= "localhost"
	puerto = 9998

	server1= SocketServer.TCPServer((host, puerto), mihandler)
	print "server corriendo"
	server1.serve_forever()

main()
		