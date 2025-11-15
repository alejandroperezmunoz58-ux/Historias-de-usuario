#Control de flujo y manejo de listas en el inventario


inventario = []
def agregar_producto():
    print("\n - Agregar un producto: ")
    nombre = input("Ingrese el nombre del producto: ")

    precio = float (input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))


    #diccionario del producto

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
#Agregar producto al menu


# agregar diccionario al inventario en lista

    inventario.append(producto)
    print("Producto agregado correctamente")
#funcion para representar el menu disponible
#--------------------------------------------------------------------------------------------------------------


#Inventario actual
def mostrar_inventario():
    print("\n - Mostrar Inventario actual -")
    if len(inventario)==0:
        print("El inventario esta vacio")
    else:
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")


#calcular estadisticas

def Calcular_estadistica ():
    print("\n Estadisticas")
    if len(inventario)==0:
        print("No hay productos para calcular una estadistica")
    else:
        valor_total = 0
        for producto in inventario:
            valor_total += producto ['precio'] * producto ['cantidad']
            print(f"Valor total del inventario: {valor_total}")
            print(f"Cantidad total de productos registrados: {len(inventario)}")

#saliendo del sistema

def Salir_del_sistema():
    print("Salir del sistema...") 
#-------------------------------------------------------------------------------------------------------

#bucle para trabajar en el menu

while True:
    print("\n== Menú Principal")
    print("1. Agregar Producto")
    print("2. Mostrar Inventario")
    print("3. Calcular Estadisticas")
    print("4. Salir del Sistema")
    opcion = input("seleccione una opcion: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        Calcular_estadistica()
    elif opcion == "4":
        Salir_del_sistema()
        break
    else:
        print("Error, porfavor ingrese un numero valido")
