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
    if l[1]=='+':
        s = xmlrpclib.ServerProxy('http://localhost:9001')
        result=s.suma(l[0],l[2])
    if l[1]=='-':
        s = xmlrpclib.ServerProxy('http://localhost:9002')
        result=s.resta(l[0],l[2])
    if l[1]=='*':
        s = xmlrpclib.ServerProxy('http://localhost:9003')
        result=s.multi(l[0],l[2])
    if l[1]=='/':
        s = xmlrpclib.ServerProxy('http://localhost:9004')
        result=s.div(l[0],l[2])
    if l[1]=='^':
        s = xmlrpclib.ServerProxy('http://localhost:9005')
        result=s.pot(l[0],l[2])
    if l[1]=='raiz':
        s = xmlrpclib.ServerProxy('http://localhost:9006')
        result=s.raiz(l[0],l[2])
    if l[1]=='log':
        s = xmlrpclib.ServerProxy('http://localhost:9007')
        result=s.log(l[0],l[2])                      
    return result
server.register_function(operacion)


server.serve_forever()


# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'div').