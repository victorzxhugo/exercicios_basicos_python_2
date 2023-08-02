#Exercicio 7 - Usando a função len() imprima em tela quantos itens existem na lista gerada no exercício 4

import random

lista_numeros = [random.randint(20, 1580) for i in range(10)]

qtd = len(lista_numeros)
print("Quantidade de itens:", qtd)