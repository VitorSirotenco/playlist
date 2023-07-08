class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self, ):
        return self._nome


    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes' #representação textual do objeto

class Filme (Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'


class Serie (Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


vingadores = Filme('vingadores', 2018, 180)

ozark = Serie('ozark', 2020, 4)

ozark.dar_like()
ozark.dar_like()
vingadores.dar_like()

filmes_e_series = [vingadores, ozark]

for programa in filmes_e_series:
    print(programa)






