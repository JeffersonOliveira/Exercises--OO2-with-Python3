class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.likes} Like(s)')


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Like(s)')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Like(s)')


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

# print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
# print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')

lista_programas = [vingadores, atlanta]
for programa in lista_programas:
    programa.imprime()