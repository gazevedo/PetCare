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
        'id': usuario['_id'],
        'loja': usuario['loja']
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


def token_decode_id(auth_header):
    token = auth_header.split(" ")[1]  # Pega o token sem o "Bearer"
    try:
        # Decodifica o token JWT e extrai o payload
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded_token.get('_id')  # Retorna o 'id' presente no token
    except jwt.ExpiredSignatureError:
        return None  # Token expirado
    except jwt.InvalidTokenError:
        return None  # Token inválido
