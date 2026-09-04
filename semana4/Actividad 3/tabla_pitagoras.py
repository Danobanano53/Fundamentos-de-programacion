tabla = []

for i in range(1, 11):
    
    fila = []
    
    for j in range(1, 11):
        resultado = i * j
        fila.append(resultado)
    
    tabla.append(fila)


def imprimir_tabla(tabla):
    
    for fila in tabla:
        
        for numero in fila:
            print(numero, end="\t")
        
        print()


def buscar_coordenanda (tabla, fila, columna):
    
    resultado = tabla[fila - 1][columna - 1]
    
    return resultado

imprimir_tabla(tabla)

fila = int(input("Ingresa el primer factor (1 al 10): "))
columna = int(input("Ingresa el segundo factor (1 al 10): "))
producto = buscar_coordenanda(tabla, fila, columna)


print(fila, "x", columna, "=", producto)

