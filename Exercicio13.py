#Exercicio 13 - Utilizando a função do exercício 11, imprima todos os números da lista como uma única string.

import random

def gerar_lista_inteiros(qtd):
    lista_numeros = [random.randint(20, 1580) for i in range(qtd)]
    return [i for i in lista_numeros if isinstance(i, int)]


qtd_itens = int(input('Insira a quantidade de itens: '))
lista_inteiros = gerar_lista_inteiros(qtd_itens)


numeros_string = ' '.join(str(numero) for numero in lista_inteiros)

print(numeros_string)