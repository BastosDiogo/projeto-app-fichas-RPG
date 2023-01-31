from model.conexao_mongo import Pymongo

class Usuario(Pymongo):
    def __init__(self) -> None:
        super().__init__()
        self.conexao_banco = self.database['usuario']

    def find_all(self,campos:dict, rejetar:dict):
        usuarios = list(self.conexao_banco.find(campos, rejetar))

        return usuarios

    def inserir_usuario(self, objeto:dict):
        try:
            self.conexao_banco.insert_one(objeto)
            return True

        except:
            return False
    
    def inserir_diversos_usuarios(self, objetos:list):
        try:
            self.conexao_banco.insert_many(objetos)
            return True

        except:
            return False

