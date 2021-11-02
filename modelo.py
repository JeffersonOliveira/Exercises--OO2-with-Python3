class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    def dar_likes(self):
        self._likes += 1

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self.duracao = duracao
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self.temporadas = temporadas
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano}'
      f' - Duracao: {vingadores.duracao} - Likes: {vingadores.likes}')

vingadores.nome = 'vingadores - guerra infinita 2'
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano}'
      f' - Duracao: {vingadores.duracao} - Likes: {vingadores.likes}')



atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}'
      f' - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')

atlanta.nome = 'atlanta novo filme 2'
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}'
      f' - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')