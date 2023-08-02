#Exercicio 9 - Crie uma lista contendo 5 nomes e adicione esta lista dentro da lista gerada no exercício 4

import random

lista_numeros = [random.randint(20, 1580) for i in range(10)]

lista_nomes = ['Victor Hugo', 'Fernando', 'João Victor', 'Henrique', 'Rafael']

lista_numeros.append(lista_nomes)

print(lista_numeros)