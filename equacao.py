#Equação de segundo grau

a = float(input("Digite o valor de a"))
b = float(input("Digite o valor de b"))
c = float(input("Digite o valor de c"))

delta = b ** 2 - 4 * a * c
if delta == 0:
    Raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print ("A raiz desta equação é", raiz1)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print ("as raízes da equação são", raiz1, "e", raiz2)
