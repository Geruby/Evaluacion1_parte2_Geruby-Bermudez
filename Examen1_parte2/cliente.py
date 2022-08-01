import xmlrpc.client

print("-----------Cliente---------")

IPServidor = "localhost"
#IPServidor = '127.0.0.1'
puertoServidor = 8080

servidor = xmlrpc.client.ServerProxy("http://{0}:{1}/".format(IPServidor,puertoServidor))

while(nombre != 'salir'):
    nombre = input('Ingrese nombre del producto para verificar precio: ')

    precio = servidor.productos(nombre.lower())

    if precio == '1':
        print('No existe ese producto')
    elif precio == '0':
        print('Saliendo de la aplicacion...')
    else:
        print('Producto: ' + nombre.upper())
        print('-------------------------')
        print('Precio: ' + precio)
        print('-------------------------')

        