#Exercicio 1: Remova strings vazias da lista de strings abaixo:
#lista_nomes = [‘Emanoela’, ‘Jonatan’, ‘’, ‘Kelly’, None, ‘Henrique’, ‘’]


lista_nomes = ['Emanoela', 'Jonatan’', '', 'Kelly', None, 'Henrique', '']

lista_nomes = [nome for nome in lista_nomes if nome and nome.strip()]

print(lista_nomes)


