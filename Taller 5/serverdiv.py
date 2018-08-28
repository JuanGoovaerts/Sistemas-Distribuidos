from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9004),
                            requestHandler=RequestHandler)
server.register_introspection_functions()
def div(x,y):
    return int(x) / int(y)
server.register_function(div)

server.serve_forever()