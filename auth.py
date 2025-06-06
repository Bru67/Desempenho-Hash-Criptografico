# Feito por: BRUNA DA SILVA CARNELOSSI e EDMUND SOARES DE SOUSA 

import getpass
import json
import hashlib
import os

# Seção 1: Autenticar e Cadastrar Usuarios

ARQUIVO_JSON = "users.json"

def inicializarDados():
    if not os.path.exists(ARQUIVO_JSON):
        # Cria o arquivo JSON com os seguintes usuarios se o arquivo não existir
        senha1 = "1234" 
        senha_em_bytes1 = senha1.encode('utf-8')
        hash_obj1 = hashlib.sha256()
        hash_obj1.update(senha_em_bytes1)
        hash_hex1 = hash_obj1.hexdigest()

        senha2 = "4321" 
        senha_em_bytes2 = senha2.encode('utf-8')
        hash_obj2 = hashlib.sha256()
        hash_obj2.update(senha_em_bytes2)
        hash_hex2 = hash_obj2.hexdigest()
        
        senha3 = "abcd" 
        senha_em_bytes3 = senha3.encode('utf-8')
        hash_obj3 = hashlib.sha256()
        hash_obj3.update(senha_em_bytes3)
        hash_hex3 = hash_obj3.hexdigest()
        
        senha4 = "dcba" 
        senha_em_bytes4 = senha4.encode('utf-8')
        hash_obj4 = hashlib.sha256()
        hash_obj4.update(senha_em_bytes4)
        hash_hex4 = hash_obj4.hexdigest()        

        usuarios = [ #obs: criar mais 2 pelo terminal
            {"nome": "bruh", "senha": hash_hex1},
            {"nome": "eddy", "senha": hash_hex2},
            {"nome": "mari", "senha": hash_hex3},
            {"nome": "luna", "senha": hash_hex4}
        ]
        with open(ARQUIVO_JSON, "w") as arquivo:
            json.dump(usuarios, arquivo, indent=4)

def menu():
    while True:
        with open("users.json", mode="r") as arquivo:
            usuarios = json.load(arquivo)

        menuInicial = input(f"\nBem-vindo \n--------------------------\n"
                            " [1] - Login\n [2] - Cadastrar \n [3] - Sair"
                            "\n--------------------------\n")

        # Login e Autenticação:
        if menuInicial == "1":
            tentativas = 0
            while tentativas < 5:
                try:
                    login = input("Login: ").strip().lower()
                    senha = getpass.getpass("Senha: ")
                    
                    # Convertendo a senha para bytes e gerando o hash SHA-256 para comparar com a senha dentro do JSON
                    senha_em_bytes = senha.encode('utf-8')
                    hash_obj = hashlib.sha256() 
                    hash_obj.update(senha_em_bytes)
                    hash_hex = hash_obj.hexdigest()
                
                
                    if any(usuario["nome"] == login and usuario["senha"] == hash_hex for usuario in usuarios):
                        print(f"\n Usuário autenticado!\n Seja Bem-vindo(a) {login}!\n")
                        autentificado = True
                        exit()
                        
                    else:
                        print(f"\n Login ou Senha incorretos, por favor tente novamente, você tem {4 - tentativas} tentativas restantes!\n")
                        tentativas += 1
                    break
                except Exception as e:
                    print(f"\n Ocorreu um erro: {e}. Por favor, tente novamente.\n")
                    tentativas += 1

        # Cadastro
        elif menuInicial == "2":
            tentativas = 0
            while tentativas < 5:
                try:
                    while True:
                        newLogin = input("Digite o seu nome (máximo 4 caracteres): ").strip()
                        if tentativas == 5:
                            print("Muitas tentativas! Acesso Bloqueado!")
                            exit()
                            
                        if len(newLogin) == 4: # Verifica se o nome do usuario tem 4 caracteres
                            break
                        else:
                            print('O login deve ter exatamente 4 caracteres. Tente novamente.\n')
                            tentativas += 1
                                                       
                            
                    # Verifica se o login já existe
                    logins_existentes = [usuario["nome"].lower() for usuario in usuarios ]
                    if newLogin.lower() in logins_existentes:
                        print("\nEste login já está em uso. Escolha outro.\n")
                        continue

                    while True:
                        newSenha = getpass.getpass("Digite uma senha (máximo 4 caracteres): ")
                        if tentativas == 5:
                            print("Muitas tentativas! Acesso Bloqueado!")
                            exit()

                        if len(newSenha) != 4:
                            print("A senha deve ter exatamente 4 caracteres. Tente novamente.\n")
                            tentativas += 1
                            
                        else:
                            break

                    confirmarSenha = getpass.getpass("Confirmar senha: ")

                    if newSenha == confirmarSenha:
                        # Convertendo a senha para bytes e gerando o hash SHA-256
                        senha_em_bytes = newSenha.encode('utf-8')   
                        hash_obj = hashlib.sha256()
                        hash_obj.update(senha_em_bytes)
                        hash_hex = hash_obj.hexdigest()
                        # Criando o novo usuário
                        newUsuario = {"nome": newLogin,
                                    "senha": hash_hex,
                                    }
                        usuarios  .append(newUsuario)
                        with open("users.json", mode="w") as arquivo:
                            json.dump(usuarios, arquivo, indent=4)
                        print("\nUsuário cadastrado com sucesso!\n")
                        break
                    else:
                        print("\nAs senhas não coincidem. Tente novamente\n")
                        tentativas += 1
                        
                except Exception as e:
                    print(f"\n Ocorreu um erro: {e}. Por favor, tente novamente.\n")
                    tentativas += 1

        # Sair
        elif menuInicial == "3":
            print("Obrigada pela visita :) \nAté Breve!\n")
            exit()
            break        

        else:
            print("\nErro! Opção inválida!\n")


inicializarDados()
menu()

