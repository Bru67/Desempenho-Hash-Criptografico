# Você tem um arquivo .txt com 4 hashes SHA-256 (um por linha).a
# As senhas são simples, por exemplo, entre 4 a 6 caracteres numéricos ou alfabéticos.
# O código tenta todas as combinações até encontrar a senha original para cada hash.

import hashlib
import itertools
import string
import time

# Carregar os hashes do arquivo
def carregar_hashes(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        return [linha.strip() for linha in f.readlines() if linha.strip()]

# Força bruta: tenta combinações até encontrar o hash correspondente
def quebrar_hash(hash_alvo, charset, tamanho_min, tamanho_max):
    for tamanho in range(tamanho_min, tamanho_max + 1):
        for tentativa in itertools.product(charset, repeat=tamanho):
            senha_teste = ''.join(tentativa)
            hash_teste = hashlib.sha256(senha_teste.encode()).hexdigest()
            if hash_teste == hash_alvo:
                return senha_teste
    return None

# Função principal com medição de tempo
def quebrar_senhas_do_arquivo(caminho_arquivo, charset=string.digits, tamanho_min=4, tamanho_max=6):
    hashes = carregar_hashes(caminho_arquivo)
    tempos_individuais = []
    inicio_total = time.time()

    for idx, hash_alvo in enumerate(hashes, 1):
        print(f"\n🔍 Quebrando senha {idx}...")
        inicio = time.time()
        senha = quebrar_hash(hash_alvo, charset, tamanho_min, tamanho_max)
        fim = time.time()
        tempo_gasto = fim - inicio
        tempos_individuais.append(tempo_gasto)
        if senha:
            print(f"✅ Senha encontrada: {senha} (tempo: {tempo_gasto:.2f} segundos)")
        else:
            print(f"❌ Não foi possível encontrar a senha (tempo: {tempo_gasto:.2f} segundos)")

    fim_total = time.time()
    tempo_total = fim_total - inicio_total
    print(f"\n⏱️ Tempo total para quebrar todas as senhas: {tempo_total:.2f} segundos")
    for i, t in enumerate(tempos_individuais, 1):
        print(f" - Senha {i}: {t:.2f} segundos")

# Exemplo de uso:
if __name__ == "__main__":
    quebrar_senhas_do_arquivo("hashes.txt", charset=string.digits, tamanho_min=4, tamanho_max=4)
