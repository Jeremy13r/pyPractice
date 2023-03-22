import mysql.connector
from decimal import Decimal
BD = mysql.connector.connect(host="localhost", user="root", password="Rotten123", database='Inventario', port='3306')
print(BD)
cursor = BD.cursor()
Opcion = 0


def bievenida():
    global Opcion
    print("Bienvenido al sistema de inventario.\n")
    print("1) Agregar un nuevo producto a la lista de productos")
    print("2) Mostrar la lista de todos los productos")
    print("3) Buscar un producto en la lista por su nombre")
    print("4) Actualizar los atributos de un producto existente")
    print("5) Eliminar un producto del inventario\n")
    Opcion = int(input("Seleccione la accion que va a efectuar: "))


def agregar():
    nombreproducto = input("Escriba el nombre del producto: ")
    categoriaproducto = input("Escriba su categoria: ")
    precioproducto = Decimal(input("Escriba el precio por unidad: "))
    stockproducto = int(input("Escriba la cantidad de unidades: "))
    nuevoproducto = {}
    nuevoproducto["Nombre"] = nombreproducto
    nuevoproducto["Categoria"] = categoriaproducto
    nuevoproducto["Precio"] = precioproducto
    nuevoproducto["Stock"] = stockproducto
    tuplaconversion = (nuevoproducto['Nombre'],
                       nuevoproducto['Categoria'],
                       nuevoproducto['Precio'],
                       nuevoproducto['Stock'])
    inserccionsql = "INSERT INTO PRODUCTOS (Nombre, Categoria, Precio, Stock)" \
                    " VALUES (%s, %s, %s, %s)"
    cursor.execute(inserccionsql, tuplaconversion)
    BD.commit()
    print("")
    print(cursor.rowcount, "producto agregado con exito")


def mostrarproductos():
    cursor.execute("SELECT * FROM Productos")
    # Recorre los resultados de la consulta y devuelve una lista de tuplas
    productos = cursor.fetchall()
    # Muestra todos los registros de la tabla Productos
    print("")
    for producto in productos:
        print(producto[0], producto[1], producto[2], producto[3], producto[4])


def buscarproducto():
    nombrebusqueda = input("Escriba el nombre del producto que desea buscar: ")
    busquedasql = "SELECT * FROM Productos WHERE Nombre = %s"
    cursor.execute(busquedasql, (nombrebusqueda,))
    resultadobusqueda = cursor.fetchall()
    print("")
    for producto in resultadobusqueda:
        print(producto[0], producto[1], producto[2], producto[3], producto[4])


def modificar():
    #while True:
    productoamodificar = input("Escriba el nombre del producto que desea modificar: ")

    print("\nEstos son los atributos que puede modificar")
    print("- Nombre")
    print("- Categoria")
    print("- Precio")
    print("- Cantidad")

    while True:
        atributomod = input("\nSeleccione una opcion: ")
        if atributomod == 'Nombre' or atributomod == 'nombre':
            nuevonombre = input("Introduzca el nuevo nombre del producto: ")
            modificarsql = "UPDATE Productos SET Nombre = %s WHERE Nombre = %s"
            valores = (nuevonombre, productoamodificar)
            cursor.execute(modificarsql, valores)
            BD.commit()
            print("")
            print(cursor.rowcount, "atributo modificado con exito")
            break

        elif atributomod == 'Categoria' or atributomod == 'categoria':
            nuevacategoria = input("Introduzca la nueva categoria del producto: ")
            modificarsql = "UPDATE Productos SET Categoria = %s WHERE Nombre = %s"
            valores = (nuevacategoria, productoamodificar)
            cursor.execute(modificarsql, valores)
            BD.commit()
            print("")
            print(cursor.rowcount, "atributo modificado con exito")
            break

        elif atributomod == 'Precio' or atributomod == 'precio':
            nuevoprecio = Decimal(input("Introduzca el nuevo precio del producto: "))
            modificarsql = "UPDATE Productos SET Precio = %s WHERE Nombre = %s"
            valores = (nuevoprecio, productoamodificar)
            cursor.execute(modificarsql, valores)
            BD.commit()
            print("")
            print(cursor.rowcount, "atributo modificado con exito")
            break

        elif atributomod == 'Cantidad' or atributomod == 'cantidad':
            nuevacantidad = int(input("Introduzca la nueva cantidad del producto: "))
            modificarsql = "UPDATE Productos SET Stock = %s WHERE Nombre = %s"
            valores = (nuevacantidad, productoamodificar)
            cursor.execute(modificarsql, valores)
            BD.commit()
            print("")
            print(cursor.rowcount, "atributo modificado con exito")
            break

        else:
            print("Esa opcion no es valida")


def eliminarproducto():
    idelete = int(input("Escriba el ID del producto que desea eliminar: "))
    eliminacionsql = "DELETE FROM Productos WHERE ID = %s"
    cursor.execute(eliminacionsql, (idelete,))
    BD.commit()
    print("")
    print(cursor.rowcount, "producto removido con exito")


bievenida()

if Opcion == 1:
    agregar()
elif Opcion == 2:
    mostrarproductos()
elif Opcion == 3:
    buscarproducto()
elif Opcion == 4:
    modificar()
elif Opcion == 5:
    eliminarproducto()
else:
    print("\nEl valor que ingreso es invalido.")


# Cierra el cursor y cierra la conexion
cursor.close()
BD.close()
