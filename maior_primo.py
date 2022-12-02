def maior_primo(n):
    for numero in reversed(range(1,n+1)):
        if all(numero%i!=0 for i in range(2,numero)):
            return numero
