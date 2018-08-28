from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import math

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9007),
                            requestHandler=RequestHandler)
server.register_introspection_functions()
def log(x,y):

    return math.log(float(x), float(y))
server.register_function(log)

server.serve_forever()
