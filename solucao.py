# Feito por: BRUNA DA SILVA CARNELOSSI e EDMUND SOARES DE SOUSA

import getpass
import json
import hashlib
import os
import base64

# Seção 3: Solução contra ataques de força bruta

ARQUIVO_JSON = "users.json"

def gerarSalt():
    return base64.b64encode(os.urandom(16)).decode('utf-8')

def inicializarDados():
    if not os.path.exists(ARQUIVO_JSON):
        # Cria o arquivo JSON com usuarios padrões se o arquivo json não existir
        senha1 = "1234" 
        salt1 = gerarSalt() 
        senhaComSalt1 = senha1 + salt1
        hashObj1 = hashlib.sha256(senhaComSalt1.encode('utf-8'))
        hash1 = hashObj1.hexdigest()

        senha2 = "4321" 
        salt2 = gerarSalt() 
        senhaComSalt2 = senha2 + salt2
        hashObj2 = hashlib.sha256(senhaComSalt2.encode('utf-8'))
        hash2 = hashObj2.hexdigest()

        usuarios = [

            {"nome": "bruh", 
             "senha":
                {"salt": salt1,
                "hash": hash1 }
                },
            {"nome": "eddi", 
             "senha":
                {"salt": salt2,
                "hash": hash2 }
                }
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

        autentificado = False

        # Login e Autenticação:
        if menuInicial == "1":
            tentativas = 0
            while tentativas < 5:
                try:
                    login = input("Login: ").strip().lower()
                    senha = getpass.getpass("Senha: ")
                    
                    user = next((usuario for usuario in usuarios if usuario["nome"] == login), None)
                    if user:
                        salt = user["senha"]["salt"]

                        # Verificando se a senha digitada + o salt é igual ao no json
                        senhaComSalt = senha + salt
                        hash_obj = hashlib.sha256(senhaComSalt.encode('utf-8')) 
                        hash = hash_obj.hexdigest()
                    
                        if user["senha"]["hash"] == hash:
                            print(f"\n Usuário autenticado!\n Seja Bem-vindo(a) {login}!\n")
                            autentificado = True
                            exit()
                        
                        else:
                            print(f"\n Login ou Senha incorretos, por favor tente novamente, você tem {4 - tentativas} tentativas restantes!\n")
                            tentativas += 1
                            continue
                    else:
                        print(f"\nUsuário {login} não encontrado. Você tem {4 - tentativas} tentativas restantes! \n")
                        tentativas += 1
                        continue
                    
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
                        # gerando um salt e concatenando com a senha para enfim, fazer o hash no formato SHA-256
                        salt = gerarSalt()
                        senhaComSalt = newSenha + salt
                        hashObj = hashlib.sha256(senhaComSalt.encode('utf-8')) 
                        hash = hashObj.hexdigest()
                    

                        # Criando o novo usuário
                        newUsuario = {"nome": newLogin,
                                    "senha": {
                                        "salt": salt,
                                        "hash": hash}
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

