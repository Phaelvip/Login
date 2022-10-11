from persistence.LoginRepository import LoginRepository

class LoginService:
    def __init__(self):
        #Dao quer dizer Data Access Object
        self.__loginDao = LoginRepository()
        pass
    
    def realizarLoginComUsuarioESenha(self, usuario, senha):
        resultset = self.__loginDao.EntrarComLogin(usuario, senha)
        if resultset != None: 
            return resultset
        else:
            return False

    
    pass