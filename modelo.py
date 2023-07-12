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

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes' #representação textual do objeto

class Filme (Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'


class Serie (Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'



class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)



vingadores = Filme('vingadores', 2018, 180)
ozark = Serie('ozark', 2020, 4)
flash = Filme('flash', 2023, 185)
demolidor = Serie('demolidor', 2016, 3)

ozark.dar_like()
ozark.dar_like()
vingadores.dar_like()
flash.dar_like()
flash.dar_like()
flash.dar_like()
demolidor.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, ozark, flash, demolidor]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da lista {len(playlist_fim_de_semana.listagem)}')

for programa in playlist_fim_de_semana.listagem:
    print(programa)






