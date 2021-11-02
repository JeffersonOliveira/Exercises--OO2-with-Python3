class Pessoa:
    tamanho_cpf = 11

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf

    def valida_cpf(self):
        return True if len(self.cpf) == __class__.tamanho_cpf else False

pe2 = Pessoa('Jess','0000000000')
print(pe2.valida_cpf())

pe = Pessoa('Jeff','00000000001')
print(pe.valida_cpf())

