#Exercicio 4 - Escreva um programa que gere uma lista com 10 números aleatórios entre 20 e 1580:(utilize a lib random)

import random

lista_numeros = [random.randint(20,1580) for i in range(10)]

print(lista_numeros)









#Forma alternativa de resolver sem utilizar expressões regulares.
"""
lista_numeros = []

for i in range(10):
    lista_numeros.append(random.randint(20,1580))

print(lista_numeros)
"""