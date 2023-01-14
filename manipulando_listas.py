#Fatias de listas

primos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

primos[1:2]

primos[2:4]

len(primos)

primos[0:7]
primos[:7]
primos[2:]

final = primos[2:]

#clonar listas

lista1 = ["vermelho", "verde", "azul"]

lista2 = lista1

lista2[0] = "rosa"

#isso acaba não clonando pois lista1 referencia lista2

#para clonar...

def clone (lista):
    clone = []
    for objeto in lista:
        clone.append(objeto)
    return clone
#forma mais fácil de fazer um clone:
lista1 = ["vermelho", "verde", "azul"]
lista1[:] #Devolve um clone da lista
lista2 = lista1[:]
lista2[0] = "Preto"

#pertinência a uma lista

"rosa" in lista1
"vermelho" in lista1

if "vermelho" in lista1:
    print("Encontrei a lista vermelha entre:", lista1)
else:
    print("Faltou, caramba!")

#Concatenação de listas

[1,2] + [3, 4]

print([1, 2, 3, 4, 5] + [6, 7, 8, 9, 10])

a = [1, 2, 3]
b = [4,5, 6,]

a + b
b + a
b + a + b

a.append("gato") #altera uma lista existente, já a concatenação gera uma nova lista

b = a + [5]


#repetição de listas

a = [1, 2, 3]

a_triplicado = a * 3

b_quintuplicado = b * 5

#remoção de elementos em listas

a = [1, 2, 3]

del a[1]

lista = ["a", "b", "c", "d", "e", "f"]
del lista[1:5]
