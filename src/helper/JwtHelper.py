import jwt
import datetime

SECRET_KEY = 'aG9zdDogcGV0Y2FkZS5jb20uYnIKZGF0YV9jcmlhY2FvOiAyMS8wNC8yMDI0CmF1dG9yOiBnYWJyaWVsIGdhcmNpYSBkZSBhemV2ZWRv'  # Guarde essa chave de maneira segura!


def gerar_token(usuario):
    """
    Função para gerar um token JWT com base no email, senha e loja_id
    """

    # Define o tempo de expiração do token
    data_atual = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    expirar_em = datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # 1 hora

    # Dados que serão codificados no JWT
    payload = {
        'id': usuario.id,
        'loja': usuario.loja
    }

    # Gera o token JWT
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def verificar_token(token):
    """
    Função para verificar o token JWT.
    Retorna o payload caso o token seja válido.
    """
    try:
        # Verifica a validade do token usando a chave secreta
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return {"message": "Token expirado!"}, 403
    except jwt.InvalidTokenError:
        return {"message": "Token inválido!"}, 403
