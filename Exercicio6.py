#Exercicio 6 - Crie um programa que use uma iteração para exibir elementos de da lista gerada no exercício 4 presentes
# em posições de índice ímpares
import random

lista_numeros = [random.randint(20,1580) for i in range(10)]

for i in range(len(lista_numeros)):
    if i % 2 == 1:
        print(lista_numeros[i])

