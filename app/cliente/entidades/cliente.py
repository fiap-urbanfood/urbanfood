class Usuario:
    def __init__(
        self, nome, email, cpf, data_aniversario, profissao, telefone, endereco
    ):
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__data_aniversario = data_aniversario
        self.__profissao = profissao
        self.__telefone = telefone
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def data_aniversario(self):
        return self.__data_aniversario

    @data_aniversario.setter
    def data_aniversario(self, data_aniversario):
        self.data_aniversario = data_aniversario

    @property
    def profissao(self):
        return self.__profissao

    @profissao.setter
    def profissao(self, profissao):
        self.profissao = profissao

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.telefone = telefone

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.endereco = endereco
