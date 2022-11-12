entrada = int(input("Digite um número inteiro"))
if ((entrada % 5) == 0) and ((entrada % 3) == 0):
    print("FizzBuzz")
elif entrada %3 == 0:
    print("FizzBuzz")
elif entrada %5 == 0:
    print("FizzBuzz")
else:
    print(entrada)
