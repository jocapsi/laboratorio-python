#repetição com FOR

frutas_exoticas = ["jabuticaba", "cupuaçu", "graviola"]

for fruta in frutas_exoticas:
    print ("Eu adoro " + fruta)

#Criar repetição em um intervalo


#em um intervalo de 0 a 19
for i in range(20):
    print(i)
#em um intervalo a partir de 10
for i in range(10, 20):
    print(i)
#em um intervalo em passos de 3, multiplos de 3
for i in range(0, 100, 3):
    print(i)
#em pares
pares = range (0, 40, 2)

for i in pares:
    print(i)
#passos de -5
numeros = range (100, 0, -5)
for x in numeros:
    print(x)

#alterando valores da lista
    #Esta dando erro nesse último código

primos = [2, 3, 5, 7, 11, 13, 17]

for i in range(len(primos)):
    print[i] = primos[i]**3
print (primos)
