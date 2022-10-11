from persistence.DbConnecion import DbConnection
from entity.Usuariopc import Usuario
from mysql.connector import Error

class LoginRepository:
    #Construtor... Não esquece carai
    def __init__(self):
        pass
    
    def EntrarComLogin(self, nome, senha):
        #con = mysql.connector.connect(host='127.0.0.1', user='root', database='ezsys',password='q9w8e7#MTB')
        db = DbConnection()
        
        usuario = None
        try:
            con = db.getConn()
            cursor = con.cursor(dictionary = True)
            valores = (nome, senha)
            cursor.execute('SELECT nome, senha FROM `ezsys`.senha WHERE nome = %s AND senha = %s', valores)
            #cursor.execute('SELECT nome, senha FROM `ez-sys`.senha WHERE nome = %s AND senha = %s', valores)
            ver = cursor.fetchone()
            print(ver)
            if(ver != None):
                usuario = Usuario(ver['nome'], ver['senha'])
            
            
            db.closeConn(cursor)    
            return usuario
        except Error as e :
            print(e)
            return usuario
   
        
    pass

    
    
   
