from xmlrpc.server import SimpleXMLRPCServer

direccionServidor = "localhost"
#direccionServidor = '127.0.0.1'
puertoServidor = 8080

print("---------Servidor---------")

def productos(nombre):
    if nombre == 'arroz':
        return '25'
    elif nombre == 'harina':
        return '30' 
    elif nombre == 'pasta':
        return '20'
    elif nombre == 'frijol':
        return '15'
    elif nombre == 'salir':
        return '0'
    else:
        return '1'

print("Esperando por cliente: ")
servidor = SimpleXMLRPCServer((direccionServidor, puertoServidor))
servidor.register_function(productos,"productos")
servidor.serve_forever()
