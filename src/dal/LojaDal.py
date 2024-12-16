from bson import ObjectId
from flask import jsonify

from src.dal.DbConnect import db
from src.model.Loja import Loja

loja_collection = db.loja

class LojaDal:
    @staticmethod
    def getLojaId(id):
        resultdb = loja_collection.find_one({"_id": ObjectId(id)})
        return resultdb

    @classmethod
    def getLojaTelefone(cls, telefone):
        resultdb = loja_collection.find_one({"telefone": telefone})
        return resultdb