class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self._likes} Like(s)')

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Like(s)')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.temporadas} Temporadas - {self._likes} Like(s)')


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()

atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()

# filmes_e_series = []  -->Criando uma lista.

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    programa.imprime()