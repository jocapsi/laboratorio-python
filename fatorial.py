#Printing fatorial numbers

entrada = int(input("Digite o valor de n: "))

resultado = 1
count = 1

while count <= entrada:
    resultado *= count
    count += 1
print(resultado)
