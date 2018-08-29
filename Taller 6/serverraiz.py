from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import math

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9006),
                            requestHandler=RequestHandler)
server.register_introspection_functions()
def op(x,y):

    return math.pow(float(x), float(1/float(y)))
server.register_function(op)

server.serve_forever()
