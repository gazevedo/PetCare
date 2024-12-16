import os
import re

from bson import ObjectId
from flask import jsonify
from werkzeug.exceptions import BadRequest, InternalServerError
from src.model.Loja import Loja
from src.dal.LojaDal import LojaDal

class LojaController:
    @staticmethod
    def getLojaId(id):

        try:
            # Verificar se o id é um ObjectId válido
            if not ObjectId.is_valid(id):
                return jsonify({"error": "ID inválido"}), 400

            # Converter id para ObjectId
            loja = LojaDal.getLojaId(id)

            if not loja:
                return jsonify({"error": "Loja não encontrada"}), 500

            return jsonify(loja), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar a loja: {str(e)}"}), 500

    def getLojaTelefone(telefone):

        try:
            print(f"Buscando loja com telefone: {telefone}")  # Log de depuração

            data = LojaDal.getLojaTele fone(telefone)

            if not data:
                return jsonify({"error": "Loja não encontrada"}), 404

            loja = Loja.to_object(data)

            return jsonify(loja.to_dict()), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar a loja: {str(e)}"}), 500

