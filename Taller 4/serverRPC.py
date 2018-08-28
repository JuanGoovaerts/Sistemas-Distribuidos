from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register pow() function; this will use the value of
# pow.__name__ as the name, which is just 'pow'.
server.register_function(pow)

# Register a function under a different name

# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'div').
class MyFuncs:
	def div(self, x, y):
		return x // y
	def add(self, x, y):		
		return x + y

	def min(self, number1, number2):
		return number1 - number2

	def mul(self, number1, number2):
		return number1 * number2
	
	def log(self, number1, number2):
		return log(number1, number2)

	def raiz(self, number1, number2):
		raiz=1/float(numero1)
		return pow(numero2, raiz)

server.register_instance(MyFuncs())

# Run the server's main loop
server.serve_forever()










