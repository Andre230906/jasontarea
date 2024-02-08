import json

# Función para cargar los datos desde el archivo JSON
def cargar_datos():
    with open('json.json') as file:
        return json.load(file)

# Función para guardar los datos en el archivo JSON
def guardar_datos(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

# Creación de un cliente
def crear_cliente():
    data = cargar_datos()
    nuevo_cliente = {
        "id": 101,
        "nombre": "Nuevo",
        "apellido1": "Cliente",
        "ciudad": "Madrid"
    }
    data["ventas"]["clientes"].append(nuevo_cliente)
    guardar_datos(data)

# Lectura de clientes
def leer_clientes():
    data = cargar_datos()
    clientes = data["ventas"]["clientes"]
    for cliente in clientes:
        print(cliente)

# Actualización de un cliente
def actualizar_cliente():
    data = cargar_datos()
    id_cliente = 101
    for cliente in data["ventas"]["clientes"]:
        if cliente["id"] == id_cliente:
            cliente["ciudad"] = "Barcelona"
    guardar_datos(data)

# Eliminación de un cliente
def eliminar_cliente():
    data = cargar_datos()
    id_cliente = 101
    data["ventas"]["clientes"] = [cliente for cliente in data["ventas"]["clientes"] if cliente["id"] != id_cliente]
    guardar_datos(data)

# Similarmente, se pueden definir funciones para crear, leer, actualizar y eliminar comerciales y pedidos.

# Ejecutar las operaciones
crear_cliente()
leer_clientes()
actualizar_cliente()
eliminar_cliente()