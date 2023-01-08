numeros = []
numero = int(input("digite um número e pressione 0 para terminar"))
while numero != 0:
    numeros.append(numero)
    numero = int(input("digite um número e 0 para terminar"))

for i in range(len(numeros)-1, -1, -1):
    print(numeros[i])

