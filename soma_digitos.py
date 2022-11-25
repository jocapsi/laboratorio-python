# soma dos digitos

receba = int(input("Digite um número inteiro: "))

soma = 0

while (receba != 0):
    resto = receba % 10
    receba = (receba - resto)// 10
    soma = soma + resto
print(soma)
