class Funcionario:
    prefixo = 'Instrutor'

    @classmethod
    def info(cls):
        return f'Esse é um {cls.prefixo}'

#funcionario = Funcionario()
#print(funcionario.info())


print(Funcionario.info())