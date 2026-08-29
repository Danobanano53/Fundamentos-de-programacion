producto1 = ""
producto2 = ""
producto3 = ""

cantidad1 = 0
cantidad2 = 0
cantidad3 = 0


ventas = 0
contador = 0


print("==============================")
print(" pinturas y ferreteria ")
print("==============================")

print(" registra 3 productos.")



for i in range(1, 4):

    print("")
    print("Producto numero", i)

    if i == 1:

        producto1 = input("Escribe el nombre del producto: ")
        cantidad1 = int(input("Escribe la cantidad: "))

    if i == 2:

        producto2 = input("Escribe el nombre del producto: ")
        cantidad2 = int(input("Escribe la cantidad: "))

    if i == 3:

        producto3 = input("Escribe el nombre del producto: ")
        cantidad3 = int(input("Escribe la cantidad: "))



ventas = 0
contador = 3

print("Productos registrados correctamente.")



opcion = 0

while opcion != 4:

   
    print("           MENU")
    print("==============================")
    print("1. Agregar producto")
    print("2. Venta")
    print("3. Revisar inventario")
    print("4. Salir")
    

    opcion = int(input("Selecciona una opcion: "))



    if opcion == 1:

        print("")
        print("----- AGREGAR PRODUCTO -----")

        print("1.", producto1)
        print("2.", producto2)
        print("3.", producto3)

        producto = int(input("Selecciona el producto: "))

        cantidad = int(input("Cantidad que deseas agregar: "))


        if producto == 1:

            cantidad1 = cantidad1 + cantidad

            print("Cantidad agregada correctamente.")


        if producto == 2:

            cantidad2 = cantidad2 + cantidad

            print("Cantidad agregada correctamente.")


        if producto == 3:

            cantidad3 = cantidad3 + cantidad

            print("Cantidad agregada correctamente.")


    if opcion == 2:

        print("")
        print("----- VENTA -----")

        print("1.", producto1)
        print("2.", producto2)
        print("3.", producto3)

        producto = int(input("Selecciona el producto: "))

        cantidad = int(input("Cantidad que deseas vender: "))


        if producto == 1:

            if cantidad <= cantidad1:

                cantidad1 = cantidad1 - cantidad

                ventas = ventas + 1

                print("Venta realizada correctamente.")

            else:

                print("No hay suficiente inventario.")


        if producto == 2:

            if cantidad <= cantidad2:

                cantidad2 = cantidad2 - cantidad

                ventas = ventas + 1

                print("Venta realizada correctamente.")

            else:

                print("No hay suficiente inventario.")


        if producto == 3:

            if cantidad <= cantidad3:

                cantidad3 = cantidad3 - cantidad

                ventas = ventas + 1

                print("Venta realizada correctamente.")

            else:

                print("No hay suficiente inventario.")


    if opcion == 3:

        print("")
        print("----- INVENTARIO -----")

        print(producto1, ":", cantidad1)
        print(producto2, ":", cantidad2)
        print(producto3, ":", cantidad3)

        print("")
        print("Productos registrados:", contador)
        print("Ventas realizadas:", ventas)


print("ferreteria y pinturas taximaroa")
print("==============================")