from bson import ObjectId
from flask import jsonify

from src.dal.DbConnect import db
from src.model.Loja import Loja

loja_collection = db.loja


class LojaDal:
    @staticmethod
    def getLojaId(id):
        loja = loja_collection.find_one({"_id": ObjectId(id)})
        loja["_id"] = str(loja["_id"])
        return loja

    @classmethod
    def getLojaTelefone(cls, telefone):
        loja = loja_collection.find_one({"telefone": telefone})
        loja["_id"] = str(loja["_id"])
        return loja
