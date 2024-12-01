import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Obter a URI do MongoDB diretamente do .env
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")  # Nome do banco de dados

# Conectar ao MongoDB
client = MongoClient(MONGO_URI)

# Especificar o banco de dados
db = client[DATABASE_NAME]  # Defina o banco de dados
