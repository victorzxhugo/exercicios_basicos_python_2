#Exercicio 14- Utilizando a função do exercício 11, crie uma lista, adicione a ela uma lista contendo 5 nomes
# e imprima todos os dados da lista como uma única string.

import random

def gerar_lista_inteiros(qtd):
    lista_numeros = [random.randint(20, 1580) for i in range(qtd)]
    return [i for i in lista_numeros if isinstance(i, int)]


qtd_itens = int(input('Insira a quantidade de itens: '))

lista_inteiros = gerar_lista_inteiros(qtd_itens)

lista_nomes = ['Victor Hugo', 'Fernando', 'João Victor', 'Henrique', 'Rafael']

lista_inteiros.append(lista_nomes)

lista_em_string = ' '.join(str(i) for i in lista_inteiros)

print(lista_em_string)