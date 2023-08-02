#Exercicio 12 - Utilize a função criada no exercício anterior e mostre em tela a soma total de todos os valores de uma lista.

import random

def gerar_lista_inteiros(qtd):
    lista_numeros = [random.randint(20, 1580) for i in range(qtd)]
    return [i for i in lista_numeros if isinstance(i, int)]


qtd_itens = int(input('Insira a quantidade de itens: '))
lista_inteiros = gerar_lista_inteiros(qtd_itens)


soma = sum(lista_inteiros)

print(f'Lista: {lista_inteiros}')
print(f'Soma total: {soma}')
