# Desempenho-Hash-Criptografico

Código feito para a atividade Somativa 2 da disciplina de Segurança de Informação

## Código base para salvar senhas em hash SHA-256
`` texto = "Olá, mundo!"``

`` texto_em_bytes = texto.encode('utf-8') ``

`` hash_obj = hashlib.sha256() ``

``hash_obj.update(texto_em_bytes)``

`` hash_hex = hash_obj.hexdigest()``

``print(hash_hex)``

## Feito por:

- Bruna da Silva Carnelossi
- Edmund Soares de Sousa
