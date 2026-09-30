import time
import os

producto1 = ""
producto2 = ""
producto3 = ""

cantidad1 = 0
cantidad2 = 0
cantidad3 = 0

ventas = 0
contador = 0


def crear_archivos():

    archivos = {
        "inventario.txt": "ARCHIVO DE INVENTARIO\n",
        "ventas.txt": "ARCHIVO DE VENTAS\n",
        "productos.txt": "ARCHIVO DE PRODUCTOS\n",
        "usuarios.txt": "ARCHIVO DE USUARIOS\n"
    }

    for nombre, contenido in archivos.items():

        if not os.path.exists(nombre):

            try:

                with open(nombre, "w") as archivo:
                    archivo.write(contenido)

                print("Archivo creado:", nombre)

            except PermissionError:

                print(
                    "No tienes permisos para crear",
                    nombre
                )

            except OSError:

                print(
                    "Error al crear",
                    nombre
                )

        else:

            print(
                "Archivo existente, se conservará:",
                nombre
            )


def cargar():

    print("\nCargando sistema...")

    for i in range(11):

        porcentaje = i * 10

        barra = (
            "#" * i +
            "-" * (10 - i)
        )

        print(
            f"\r[{barra}] {porcentaje}%",
            end=""
        )

        time.sleep(0.2)

    print("\nCarga completa.")


def capturar_fecha():

    while True:

        try:

            fecha = input(
                "\nIngresa la fecha de operación "
                "(dia/mes/año): "
            )

            partes = fecha.split("/")

            if len(partes) != 3:

                print(
                    "Formato incorrecto. "
                    "Usa dia/mes/año."
                )

                continue

            dia = int(partes[0])
            mes = int(partes[1])
            anio = int(partes[2])

            if dia < 1 or dia > 31:

                print(
                    "El día debe estar "
                    "entre 1 y 31."
                )

                continue

            if mes < 1 or mes > 12:

                print(
                    "El mes debe estar "
                    "entre 1 y 12."
                )

                continue

            if anio < 2000 or anio > 2100:

                print(
                    "El año debe estar "
                    "entre 2000 y 2100."
                )

                continue

            Fecha = dia, mes, anio

            print(
                "Fecha registrada:",
                Fecha
            )

            return Fecha

        except ValueError:

            print(
                "Error: utiliza números "
                "con el formato dia/mes/año."
            )


def guardar_archivo(nombre_archivo, texto, Fecha):

    try:

        with open(nombre_archivo, "a") as archivo:

            archivo.write(
                f"Fecha: {Fecha}\n"
            )

            archivo.write(
                texto + "\n"
            )

        print(
            "Información guardada correctamente."
        )

    except FileNotFoundError:

        print(
            "El archivo no existe."
        )

    except PermissionError:

        print(
            "No tienes permisos para modificar "
            "el archivo."
        )

    except OSError:

        print(
            "Error del sistema al escribir "
            "el archivo."
        )


def guardar_productos():

    try:

        with open(
            "productos.txt",
            "w"
        ) as archivo:

            archivo.write(
                "ARCHIVO DE PRODUCTOS\n"
            )

            archivo.write(
                f"producto1|{producto1}|{cantidad1}\n"
            )

            archivo.write(
                f"producto2|{producto2}|{cantidad2}\n"
            )

            archivo.write(
                f"producto3|{producto3}|{cantidad3}\n"
            )

        print(
            "Productos guardados correctamente."
        )

    except PermissionError:

        print(
            "No tienes permisos para guardar "
            "los productos."
        )

    except OSError:

        print(
            "Error al guardar los productos."
        )


def cargar_productos():

    global producto1
    global producto2
    global producto3
    global cantidad1
    global cantidad2
    global cantidad3
    global contador

    try:

        with open(
            "productos.txt",
            "r"
        ) as archivo:

            lineas = archivo.readlines()

        productos_encontrados = 0

        for linea in lineas:

            linea = linea.strip()

            partes = linea.split("|")

            if len(partes) != 3:

                continue

            nombre_variable = partes[0]
            nombre_producto = partes[1]
            cantidad = int(partes[2])

            if nombre_variable == "producto1":

                producto1 = nombre_producto
                cantidad1 = cantidad

                productos_encontrados += 1

            elif nombre_variable == "producto2":

                producto2 = nombre_producto
                cantidad2 = cantidad

                productos_encontrados += 1

            elif nombre_variable == "producto3":

                producto3 = nombre_producto
                cantidad3 = cantidad

                productos_encontrados += 1

        if productos_encontrados == 3:

            contador = 3

            print(
                "\nProductos anteriores "
                "cargados correctamente."
            )

            print(
                producto1,
                ":",
                cantidad1
            )

            print(
                producto2,
                ":",
                cantidad2
            )

            print(
                producto3,
                ":",
                cantidad3
            )

            return True

        else:

            return False

    except FileNotFoundError:

        return False

    except ValueError:

        print(
            "Error: los datos guardados "
            "de los productos son incorrectos."
        )

        return False

    except PermissionError:

        print(
            "No tienes permisos para leer "
            "productos.txt."
        )

        return False

    except OSError:

        print(
            "Error al leer productos.txt."
        )

        return False


def leer_archivo():

    archivos = [
        "inventario.txt",
        "ventas.txt",
        "productos.txt",
        "usuarios.txt"
    ]

    print(
        "\n----- ARCHIVOS DISPONIBLES -----"
    )

    for i in range(len(archivos)):

        print(
            i + 1,
            ".",
            archivos[i]
        )

    try:

        opcion = int(
            input(
                "\nSelecciona el archivo "
                "que deseas abrir: "
            )
        )

        if opcion < 1 or opcion > len(archivos):

            print(
                "Opción no válida."
            )

            return

        nombre = archivos[opcion - 1]

        print(
            "\n----- CONTENIDO -----"
        )

        with open(
            nombre,
            "r"
        ) as archivo:

            contenido = archivo.read()

            print(contenido)

    except ValueError:

        print(
            "Debes utilizar un número."
        )

    except FileNotFoundError:

        print(
            "El archivo no existe."
        )

    except PermissionError:

        print(
            "No tienes permisos para "
            "leer este archivo."
        )

    except OSError:

        print(
            "Error al leer el archivo."
        )


def agregar_producto(Fecha):

    global cantidad1
    global cantidad2
    global cantidad3

    print(
        "\n----- AGREGAR PRODUCTO -----"
    )

    print(
        "1.",
        producto1
    )

    print(
        "2.",
        producto2
    )

    print(
        "3.",
        producto3
    )

    try:

        producto = int(
            input(
                "Selecciona el producto: "
            )
        )

        cantidad = int(
            input(
                "Cantidad que deseas agregar: "
            )
        )

        if cantidad <= 0:

            print(
                "La cantidad debe ser "
                "mayor que cero."
            )

            return

        if producto == 1:

            cantidad1 = cantidad1 + cantidad

            texto = (
                f"Se agregaron {cantidad} "
                f"unidades de {producto1}. "
                f"Inventario actual: {cantidad1}"
            )

            guardar_archivo(
                "inventario.txt",
                texto,
                Fecha
            )

        elif producto == 2:

            cantidad2 = cantidad2 + cantidad

            texto = (
                f"Se agregaron {cantidad} "
                f"unidades de {producto2}. "
                f"Inventario actual: {cantidad2}"
            )

            guardar_archivo(
                "inventario.txt",
                texto,
                Fecha
            )

        elif producto == 3:

            cantidad3 = cantidad3 + cantidad

            texto = (
                f"Se agregaron {cantidad} "
                f"unidades de {producto3}. "
                f"Inventario actual: {cantidad3}"
            )

            guardar_archivo(
                "inventario.txt",
                texto,
                Fecha
            )

        else:

            print(
                "Producto no válido."
            )

            return

        guardar_productos()

    except ValueError:

        print(
            "Debes introducir números enteros."
        )


def realizar_venta(Fecha):

    global cantidad1
    global cantidad2
    global cantidad3
    global ventas

    print(
        "\n----- VENTA -----"
    )

    print(
        "1.",
        producto1
    )

    print(
        "2.",
        producto2
    )

    print(
        "3.",
        producto3
    )

    try:

        producto = int(
            input(
                "Selecciona el producto: "
            )
        )

        cantidad = int(
            input(
                "Cantidad que deseas vender: "
            )
        )

        if cantidad <= 0:

            print(
                "La cantidad debe ser "
                "mayor que cero."
            )

            return

        if producto == 1:

            if cantidad <= cantidad1:

                cantidad1 = cantidad1 - cantidad

                ventas = ventas + 1

                print(
                    "Venta realizada correctamente."
                )

                texto = (
                    f"Venta de {cantidad} "
                    f"unidades de {producto1}. "
                    f"Inventario restante: "
                    f"{cantidad1}"
                )

                guardar_archivo(
                    "ventas.txt",
                    texto,
                    Fecha
                )

                guardar_productos()

            else:

                print(
                    "No hay suficiente inventario."
                )

        elif producto == 2:

            if cantidad <= cantidad2:

                cantidad2 = cantidad2 - cantidad

                ventas = ventas + 1

                print(
                    "Venta realizada correctamente."
                )

                texto = (
                    f"Venta de {cantidad} "
                    f"unidades de {producto2}. "
                    f"Inventario restante: "
                    f"{cantidad2}"
                )

                guardar_archivo(
                    "ventas.txt",
                    texto,
                    Fecha
                )

                guardar_productos()

            else:

                print(
                    "No hay suficiente inventario."
                )

        elif producto == 3:

            if cantidad <= cantidad3:

                cantidad3 = cantidad3 - cantidad

                ventas = ventas + 1

                print(
                    "Venta realizada correctamente."
                )

                texto = (
                    f"Venta de {cantidad} "
                    f"unidades de {producto3}. "
                    f"Inventario restante: "
                    f"{cantidad3}"
                )

                guardar_archivo(
                    "ventas.txt",
                    texto,
                    Fecha
                )

                guardar_productos()

            else:

                print(
                    "No hay suficiente inventario."
                )

        else:

            print(
                "Producto no válido."
            )

    except ValueError:

        print(
            "Debes introducir números enteros."
        )


def revisar_inventario():

    print(
        "----- INVENTARIO -----"
    )

    print(
        producto1,
        ":",
        cantidad1
    )

    print(
        producto2,
        ":",
        cantidad2
    )

    print(
        producto3,
        ":",
        cantidad3
    )

    print()

    print(
        "Productos registrados:",
        contador
    )

    print(
        "Ventas realizadas:",
        ventas
    )


def mostrar_menu():

    menu = [
        ["1", "Agregar producto"],
        ["2", "Venta"],
        ["3", "Revisar inventario"],
        ["4", "Leer archivos"],
        ["5", "Guardar reporte"],
        ["6", "Salir"]
    ]

    print(
        " MENU"
    )

    for fila in menu:

        print(
            fila[0],
            ".",
            fila[1]
        )

    print(
        "=============================="
    )


crear_archivos()


usuario = input(
    "Registre su usuario o nickname: "
)


print(
    f"Bienvenido al sistema, {usuario}."
)

print(
    "Pinturas y Ferretería Taximaroa"
)

print(
    "================================"
)


cargar()


Fecha = capturar_fecha()


if cargar_productos():

    print(
        "\nNo es necesario registrar "
        "los productos nuevamente."
    )

else:

    print(
        "\nNo existen productos guardados."
    )

    print(
        "Registra 3 productos."
    )

    for i in range(1, 4):

        print(
            "Producto número",
            i
        )

        while True:

            try:

                if i == 1:

                    producto1 = input(
                        "Escribe el nombre "
                        "del producto: "
                    )

                    cantidad1 = int(
                        input(
                            "Escribe la cantidad: "
                        )
                    )

                    if cantidad1 <= 0:

                        print(
                            "La cantidad debe "
                            "ser mayor que cero."
                        )

                        continue

                elif i == 2:

                    producto2 = input(
                        "Escribe el nombre "
                        "del producto: "
                    )

                    cantidad2 = int(
                        input(
                            "Escribe la cantidad: "
                        )
                    )

                    if cantidad2 <= 0:

                        print(
                            "La cantidad debe "
                            "ser mayor que cero."
                        )

                        continue

                elif i == 3:

                    producto3 = input(
                        "Escribe el nombre "
                        "del producto: "
                    )

                    cantidad3 = int(
                        input(
                            "Escribe la cantidad: "
                        )
                    )

                    if cantidad3 <= 0:

                        print(
                            "La cantidad debe "
                            "ser mayor que cero."
                        )

                        continue

                break

            except ValueError:

                print(
                    "La cantidad debe "
                    "ser un número."
                )

    contador = 3

    guardar_productos()

    guardar_archivo(
        "productos.txt",
        f"Productos registrados: "
        f"{producto1}, "
        f"{producto2}, "
        f"{producto3}",
        Fecha
    )

    print(
        "Productos registrados correctamente."
    )


opcion = 0


while opcion != 6:

    mostrar_menu()

    try:

        opcion = int(
            input(
                "Selecciona una opción: "
            )
        )

    except ValueError:

        print(
            "Selecciona una opción "
            "utilizando números."
        )

        continue

    if opcion == 1:

        cargar()

        agregar_producto(Fecha)

    elif opcion == 2:

        cargar()

        realizar_venta(Fecha)

    elif opcion == 3:

        cargar()

        revisar_inventario()

    elif opcion == 4:

        cargar()

        leer_archivo()

    elif opcion == 5:

        cargar()

        texto = (
            f"Inventario actual: "
            f"{producto1}={cantidad1}, "
            f"{producto2}={cantidad2}, "
            f"{producto3}={cantidad3}. "
            f"Ventas realizadas: {ventas}"
        )

        guardar_archivo(
            "inventario.txt",
            texto,
            Fecha
        )

    elif opcion == 6:

        print(
            f"Hasta luego, {usuario}."
        )

        print(
            "Ferretería y Pinturas Taximaroa"
        )

    else:

        print(
            "Opción no válida."
        )


print(
    "\nPrograma finalizado."
)