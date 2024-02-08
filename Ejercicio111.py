import json

def cargar_datos():
    with open('data.json') as file:
        return json.load(file)

def guardar_datos(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def crear_cliente(cliente):
    data = cargar_datos()
    data['clientes'].append(cliente)
    guardar_datos(data)

def obtener_clientes():
    data = cargar_datos()
    return data['clientes']

def actualizar_cliente(id_cliente, nuevo_nombre):
    data = cargar_datos()
    for cliente in data['clientes']:
        if cliente['id'] == id_cliente:
            cliente['nombre'] = nuevo_nombre
    guardar_datos(data)

def eliminar_cliente(id_cliente):
    data = cargar_datos()
    data['clientes'] = [cliente for cliente in data['clientes'] if cliente['id'] != id_cliente]
    guardar_datos(data)

# Crear un nuevo cliente
nuevo_cliente = {'id': 1, 'nombre': 'Juan', 'apellido': 'Perez'}
crear_cliente(nuevo_cliente)

# Mostrar la lista de clientes
print(obtener_clientes())

# Actualizar un cliente
actualizar_cliente(1, 'Juanito')

# Eliminar un cliente
eliminar_cliente(1)
