#Exercicio 8 - Usando a função len() imprima em tela quantos caracteres cada item da lista gerada no exercício possui:

import random

lista_numeros = [random.randint(20, 1580) for i in range(10)]

for i in lista_numeros:
    print(f"{i}: Tem {len(str(i))} caracteres")