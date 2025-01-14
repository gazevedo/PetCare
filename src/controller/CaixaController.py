from datetime import datetime

from bson import ObjectId
from flask import jsonify
from src.dal.CaixaDao import CaixaDao

class CaixaController:
    @staticmethod
    def buscar_por_id(id):
        """
        Busca um caixa pelo ID.
        """
        try:
            # Verificar se o ID é válido
            if not ObjectId.is_valid(id):
                return jsonify({"error": "ID inválido"}), 400

            # Buscar o caixa no banco de dados
            caixa = CaixaDao.buscar_por_id(ObjectId(id))

            if not caixa:
                return jsonify({"error": "Caixa não encontrado"}), 404

            # Converter o `_id` para string antes de retornar
            caixa["_id"] = str(caixa["_id"])
            return jsonify(caixa), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar o caixa: {str(e)}"}), 500

    @staticmethod
    def buscar_tipos_movimentacao():
        try:
            return CaixaDao.buscar_tipos_movimentacao()
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar tipos de movimentacao: {str(e)}"}), 500

    @staticmethod
    def registrar_movimentacao(caixa):
        try:
            # Verificar se a lista de movimentações não está vazia
            movimentacoes = caixa.get("movimentacoes")

            if not movimentacoes or len(movimentacoes) == 0:
                return jsonify({"error": "A lista de movimentações não pode estar vazia"}), 400

            primeira_movimentacao = movimentacoes[0]
            movimentacoes_cadastradas  = CaixaDao.buscar_tipos_movimentacao()

            #valida data
            try:
                datetime.strptime(primeira_movimentacao["data"], "%Y-%m-%dT%H:%M:%S.%fZ")
            except ValueError:
                return jsonify({"error": "A data de abertura está no formato incorreto, use o formato: "
                                         "YYYY-MM-DDTHH:MM:SS.sssZ"}), 400

            # Validar o valor
            valor = primeira_movimentacao.get("valor")
            if valor is None:
                return jsonify({"error": "O valor da movimentação é obrigatório"}), 400

            # validar tipo
            tipos_validos = [mov["tipo"] for mov in movimentacoes_cadastradas]
            if primeira_movimentacao["tipo"] not in tipos_validos:
                return jsonify({"error": "Tipo de movimentação inválido"}), 400

            if primeira_movimentacao["tipo"] == "0": #abertura
                return CaixaController.registra_abertura(caixa)
            elif primeira_movimentacao["tipo"] == "1": #fechamento
                return CaixaController.registra_fechamento(caixa)
            else:
                return CaixaController.registra_movimentaccao(caixa)
                pass
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao registrar movimentação: {str(e)}"}), 500

    @staticmethod
    def buscar_movimentacoes(json):
        try:
            caixaId = json.args.get('caixaId')
            usuarioId = json.args.get('usuarioId')
            inicio = json.args.get('inicio')
            fim = json.args.get('fim')

            filtro = {}
            if caixaId:
                filtro['caixaId'] = caixaId
            if usuarioId:
                filtro['usuarioId'] = usuarioId
            if inicio:
                filtro['data'] = {"$gte": datetime.fromisoformat(inicio)}
            if fim:
                filtro['data'] = {"$lte": datetime.fromisoformat(fim)}

            movimentacoes = CaixaDao.buscar_movimentacoes(filtro)
            return jsonify([mov.__dict__ for mov in movimentacoes]), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar os tipos de movimentacao: {str(e)}"}), 500

    @staticmethod
    def registra_abertura(caixa):
        try:
            # Verificar se `caixaId` é diferente de nulo
            if caixa.get("caixaId") is not None:
                return jsonify({"error": "Já existe um caixa aberto. Feche o caixa atual antes de abrir outro."}), 400

            # Validar `lojaID`
            if not caixa.get("lojaID"):
                return jsonify({"error": "O campo 'lojaID' é obrigatório"}), 400

            # Validar `usuarioId`
            if not caixa.get("usuarioId"):
                return jsonify({"error": "O campo 'usuarioId' é obrigatório"}), 400

            CaixaController.salva_movimentacao(caixa)

        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao registrar abertura: {str(e)}"}), 500

    @staticmethod
    def registra_fechamento(caixa):
        # Verificar se `caixaId` é nulo
        if not caixa.get("caixaId"):
            return jsonify({"error": "O campo 'caixaId' é obrigatório"}), 400

        # Validar `lojaID`
        if not caixa.get("lojaID"):
            return jsonify({"error": "O campo 'lojaID' é obrigatório"}), 400

        # Validar `usuarioId`
        if not caixa.get("usuarioId"):
            return jsonify({"error": "O campo 'usuarioId' é obrigatório"}), 400

        caixa = CaixaDao.buscar_por_id(ObjectId(id))

        if not caixa:
            return jsonify({"error": "Caixa não encontrado"}), 404
        else:
            CaixaController.salva_movimentacao(caixa)


    @staticmethod
    def registra_movimentaccao( caixa):
        # Verificar se `caixaId` é nulo
        if not caixa.get("caixaId"):
            return jsonify({"error": "O campo 'caixaId' é obrigatório"}), 400

        # Validar `lojaID`
        if not caixa.get("lojaID"):
            return jsonify({"error": "O campo 'lojaID' é obrigatório"}), 400

        # Validar `usuarioId`
        if not caixa.get("usuarioId"):
            return jsonify({"error": "O campo 'usuarioId' é obrigatório"}), 400

        caixa = CaixaDao.buscar_por_id(ObjectId(id))

        if not caixa:
            return jsonify({"error": "Caixa não encontrado"}), 404
        else:
            CaixaController.salva_movimentacao(caixa)

    @staticmethod
    def salva_movimentacao(caixa):
        try:
            # Salvar a movimentação no MongoDB usando CaixaDao
            caixa = CaixaDao.salvar_movimentacao(caixa)

            # Se a movimentação foi salva com sucesso
            return jsonify({"message": "Movimentação registrada com sucesso", "movimentacao": caixa}), 200

        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao salvar a movimentação: {str(e)}"}), 500

 
        
