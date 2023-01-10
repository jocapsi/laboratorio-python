def remove_repetidos(lista):
    # Cria um conjunto a partir da lista para remover os elementos repetidos
    sem_repetidos = set(lista)
    # Ordena o conjunto criado
    sem_repetidos = sorted(sem_repetidos)
    # Converte o conjunto de volta em uma lista e retorna a lista resultante
    return list(sem_repetidos)

#Testar código

lista = [2, 3, 2, 1, 5, 3, 4]
lista_sem_repetidos = remove_repetidos(lista)
print(lista_sem_repetidos)  # Imprime [1, 2, 3, 4, 5]
