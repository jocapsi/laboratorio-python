#Calculando a distancia das coordenadas
import math

ax = int(input("Digite as coodernadas x do primeiro plano"))
ay = int(input("Digite as coodernadas y do primeiro plano"))
bx = int(input("Digite as coodernadas x do segundo plano"))
by = int(input("Digite as coodernadas y do segundo plano"))

distancia = math.sqrt((bx) - (ax)**2 + (by - ay)**2)

if distancia >= 10:
    print("longe")
if distancia < 10:
    print("perto")
