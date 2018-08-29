from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
result =0
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
def operacion(l):
    print l
    if l=='+':
        result='http://localhost:9001'
    if l=='-':
        result='http://localhost:9002'
    if l=='*':
        result='http://localhost:9003'
    if l=='/':
        result='http://localhost:9004'
    if l=='^':
        result='http://localhost:9005'
    if l=='raiz':
        result='http://localhost:9006'
    if l=='log':
        result='http://localhost:9007'                  
    return result
server.register_function(operacion)



server.serve_forever()


# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'div').