#Exercicio 10 - Crie um programa para remover tudo que não for do tipo inteiro da lista gerada no exercício 9.

import random

lista_numeros = [random.randint(20, 1580) for i in range(10)]

lista_nomes = ['Victor Hugo', 'Fernando', 'João Victor', 'Henrique', 'Rafael']

lista_numeros.append(lista_nomes)

lista_numeros = [i for i in lista_numeros if isinstance(i,int)]

print(lista_numeros)