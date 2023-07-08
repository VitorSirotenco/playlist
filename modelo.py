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

class Filme (Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao



class Serie (Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme('vingadores', 2018, 180)

ozark = Serie('ozark', 2020, 4)


print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} Likes: {vingadores.likes}')
print(f'Nome: {ozark.nome} - Ano: {ozark.ano} - Temporadas: {ozark.temporadas} - Likes: {ozark.likes}')



