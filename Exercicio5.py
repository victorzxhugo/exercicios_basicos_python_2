#5 - Escreva um programa para exibir apenas os números da lista gerada no exercício 4 que satisfaçam as seguintes condições:
#- O número deve ser divisível por cinco
#- Se o número for maior que 95 e menor que 150 e, pule-o e passe para o próximo número
#- Se o número for maior que 1500, pare o loop


import random

lista_numeros = [random.randint(20,1580) for i in range(10)]

print(lista_numeros)

lista_validacao = []
for numero in lista_numeros:

    if numero > 1500:
        break

    if numero % 5 == 0:
        if 95 < numero < 150:
            continue
        else:
            lista_validacao.append(numero)

print(lista_validacao)