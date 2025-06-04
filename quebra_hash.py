# Feito por: BRUNA DA SILVA CARNELOSSI e EDMUND SOARES DE SOUSA

import hashlib
import itertools
import string
import time
import json

# Seção 2: Quebra de Hashes com força bruta

# Criando um charset para aceitar letras, numeros e caracteres especiais
charset = string.digits +string.ascii_letters + string.punctuation  

# Carregar os hashes do arquivo users.json
def carregar_hashes(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        usuarios = json.load(f)
        caminho_return = []

        for usuario in usuarios:
            senha = usuario.get('senha')
            if isinstance(senha, dict): # Para solucao.py --> verifica se 'senha' é um dicionário
                hash = senha.get('hash')
                if hash:
                    caminho_return.append(hash)
            elif isinstance(senha, str): # Para auth.py --> verifica se 'senha' é uma string
                caminho_return.append(senha)
        return caminho_return
    
# Força bruta: tenta combinações até encontrar o hash correspondente
def quebrar_hash(hash_alvo, charset, tamanho_min, tamanho_max):
    for tamanho in range(tamanho_min, tamanho_max + 1):
        for tentativa in itertools.product(charset, repeat=tamanho):
            senha_teste = ''.join(tentativa)
            hash_teste = hashlib.sha256(senha_teste.encode('utf-8')).hexdigest()
            if hash_teste == hash_alvo:
                return senha_teste
    return None

# Função principal com medição de tempo
def quebrar_senhas_do_arquivo(caminho_arquivo, charset, tamanho_min, tamanho_max):
    try:
        hashes = carregar_hashes(caminho_arquivo)
        tempos_individuais = []
        inicio_total = time.time()

        for idx, hash_alvo in enumerate(hashes, 1):
            print(f"\nQuebrando senha {idx}...")
            inicio = time.time()
            senha = quebrar_hash(hash_alvo, charset=charset, tamanho_min=4, tamanho_max=4)
            fim = time.time()
            tempo_gasto = fim - inicio
            tempos_individuais.append(tempo_gasto)
            if senha:
                print(f"Senha encontrada com sucesso: {senha} (tempo: {tempo_gasto:.2f} segundos)")
            else:
                print(f"Não foi possível encontrar a senha (tempo: {tempo_gasto:.2f} segundos)")

        fim_total = time.time()
        tempo_total = fim_total - inicio_total
        print(f"\n Tempo total para quebrar todas as senhas: {tempo_total:.2f} segundos")
        for i, t in enumerate(tempos_individuais, 1):
            print(f" - Senha {i}: {t:.2f} segundos")

    except Exception as e:
        print(f"\n Ocorreu um erro: {e}.\n")


quebrar_senhas_do_arquivo("users.json", charset, tamanho_min=4, tamanho_max=4)
