#2 - Imprima as palavras que contenham letras e números juntos da frase abaixo:
#frase = ‘Paulo é d4veloper e um b0m musico‘

import re

frase = 'Paulo é d4veloper e um b0m musico'

palavras_com_letnum = re.findall(r'\b\w*\d\w*\b', frase)

print(palavras_com_letnum)





#Forma alternativa de resolver sem utilizar expressões regulares.
"""
frase = 'Paulo é d4veloper e um b0m musico'

palavras_com_letnum = []

palavras = frase.split()

for palavra in palavras:
    possui_letras_e_numeros = False
    for caractere in palavra:
        if caractere.isalpha() and not possui_letras_e_numeros:
            possui_letras_e_numeros = True
        elif caractere.isdigit() and possui_letras_e_numeros:
            palavras_com_letnum.append(palavra)
            break

print(palavras_com_letnum)
"""