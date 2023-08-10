class Animal:
    pass

    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        return print('Animal emitiu som')


class Cachorro(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca

    def obter_raca(self):
        return self.__raca

    def emitir_som(self):
        return print('Au au')

class Gato(Animal):
    def __init__(self, nome, especie, pelagem):
        super().__init__(nome, especie)
        self.__pelagem = pelagem

    def obter_pelagem(self):
        return self.__pelagem

    def emitir_som(self):
        return print('Miau')


doberman = Cachorro('Bob','Cachorro','Doberman')
persa = Gato('Safira','Gato','Persa')


print(f'------------\nEmitindo som: ')
doberman.emitir_som()
print(f'Nome: {doberman.nome}\nEspecie: {doberman.especie}\nRaça: {doberman.obter_raca()}\n____________')

print(f'Emitindo som: ')
persa.emitir_som()
print(f'Nome: {persa.nome}\nEspecie: {persa.especie}\nRaça: {persa.obter_pelagem()}\n____________')










