# Entrada de datos con validación

# Solicitar el nombre (cadena de texto)
nombre = input("Ingrese el nombre del producto: ")

# Solicitar el precio (float), validando que el usuario ingrese un número
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")

# Solicitar la cantidad (int), validando que el usuario ingrese un número entero
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero válido para la cantidad.")


print("\n--- Datos del producto ---")
print(f"Nombre: {nombre}")
print(f"Precio: {precio}")
print(f"Cantidad: {cantidad}")



# Calcular el costo_total como operacion matematica

costo_total = precio * cantidad

#Impresion de resultados en la consola


print(f"producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

#Documentacion del codigo
#Este programa le solicita al usuario que ingrese el nombre, precio y cantidad del producto
#valida que los datos sean correctos, se calcula el precio o costo total y los muestra en pantalla (consola)


