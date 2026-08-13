nombre = input("Ingrese su nombre: ")
d1 = float(input("cuantas horas dedicas a las redes socciales: "))
d2 = float(input("cuantas horas dedicas a juegos en linea: "))
d3 = float(input("cuantas horas dedicas a apps de streaming: "))
d4 = float(input("cuantas horas dedicas a llamadas: "))
d5 = float(input("cuantas horas dedicas a apps de mensajeria: "))

horas = (d1 + d2 + d3 + d4 + d5)
porcentaje = (horas*100)/(24)

print("Hola", nombre, "usted dedica un total de", horas, "horas a las redes sociales, juegos en linea, apps de streaming, llamadas y apps de mensajeria, lo que representa un porcentaje del", porcentaje, "% de su dia.")