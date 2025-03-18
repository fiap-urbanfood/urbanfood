class Usuario:
    def __init__(self, nome, categoria):
        self.__nome = nome
        self.__categoria = categoria

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria
