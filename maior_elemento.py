entrada = []
entrada2 = int(input("Digite uma lista de números e pressione 0 para terminar"))
while entrada2 != 0:
    entrada.append(entrada2)
    entrada2 = int(input("Digite uma lista de números e pressione 0 para terminar"))
    
def maior_elemento(entrada):
  for elemento in entrada:
    return max(entrada)

print("O maior elemento é:", maior_elemento(entrada))
