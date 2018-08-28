from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9001),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register pow() function; this will use the value of


# Register a function under a different name
def suma(x,y):

    return int(x) + int(y)
server.register_function(suma)

# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'div').


# Run the server's main loop
server.serve_forever()
