def maximo(n1, n2, n3):
    primeiro = n1
    segundo = n2
    terceiro = n3
    if (primeiro > segundo) and (primeiro > terceiro):
        return primeiro   
    if (segundo > primeiro) and (segundo > terceiro):
        return segundo
    if (terceiro > primeiro) and (terceiro > segundo):
        return terceiro
    if (primeiro == segundo) and (primeiro > terceiro):
        return primeiro
    if (primeiro == terceiro) and (primeiro > segundo):
        return primeiro
    if (segundo == terceiro) and (segundo > primeiro):
        return segundo
    if (primeiro == segundo) and (primeiro == terceiro):
        return primeiro
