#Exercicio 11- Utilizando os códigos criados na resolução dos exercícios anteriores, crie uma função que retorne
# uma lista de itens inteiros e que receba a quantidade de itens a serem gerados por parâmetro.

import random

def gerar_lista_inteiros(qtd):
    lista_numeros = [random.randint(20, 1580) for i in range(qtd)]
    return [i for i in lista_numeros if isinstance(i, int)]


qtd_itens = int(input('Insira a quantidade de itens: '))
lista_inteiros = gerar_lista_inteiros(qtd_itens)

print(lista_inteiros)
