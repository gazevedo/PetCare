import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


class DBConnection:
    def __init__(self):
        # Carregar URI e nome do banco de dados do arquivo .env
        self.MONGO_URI = os.getenv("MONGO_URI")
        self.DATABASE_NAME = os.getenv("DATABASE_NAME")

        # Estabelecendo a conexão com o MongoDB
        self.client = MongoClient(self.MONGO_URI)
        self.db = self.client[self.DATABASE_NAME]

    def connect(self):
        """
        Retorna a instância do banco de dados para uso nos controladores
        """
        return self.db
