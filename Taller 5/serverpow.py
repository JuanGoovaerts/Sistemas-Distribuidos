from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9005),
                            requestHandler=RequestHandler)
server.register_introspection_functions()
def pot(x,y):

    return int(x) ** int(y)
server.register_function(pot)

server.serve_forever()
