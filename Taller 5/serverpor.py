from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9003),
                            requestHandler=RequestHandler)
server.register_introspection_functions()
def multi(x,y):

    return int(x) * int(y)
server.register_function(multi)

server.serve_forever()
