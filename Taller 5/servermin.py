from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9002),
                            requestHandler=RequestHandler)
server.register_introspection_functions()
def resta(x,y):

    return int(x) - int(y)
server.register_function(resta)

server.serve_forever()