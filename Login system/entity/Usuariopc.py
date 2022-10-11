class Usuario:
    
    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha
    
    
    def getNome(self):
        return self.__nome
    
    def getSenha(self):
        return self.__senha
    
    def __str__(self):
        return "Nome: " + self.__nome + ", Senha: " + self.__senha