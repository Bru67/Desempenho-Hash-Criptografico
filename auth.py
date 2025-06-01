import getpass
import json
import os

# Seção 1: Autenticar e Cadastrar Usuarios

ARQUIVO_JSON = "users.json"

def inicializarDados():
    if not os.path.exists(ARQUIVO_JSON):
        usuarios = [
            {"nome": "Bruna", "senha": "1234"},
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

        # Login
        if menuInicial == "1":
            tentativas = 0
            while tentativas < 5:
                login = input("Login: ").strip().lower()
                senha = getpass.getpass("Senha: ")
                if any(usuario["nome"] == login and usuario["senha"] == senha for usuario in usuarios):
                    print(f"\n Usuário autenticado!\n Seja Bem-vindo(a) {login}!\n")
                    autentificado = True
                    
                    break
                else:
                    print(f"\n Login ou Senha incorretos, por favor tente novamente, você tem {4 - tentativas} tentativas restantes!\n")
                    tentativas += 1

        # Cadastro
        elif menuInicial == "2":
            tentativas = 0
            while tentativas < 5:
                newLogin = input("Digite o seu nome (login): ").strip()
                logins_existentes = [usuario["login"].lower() for usuario in usuarios ]
                if newLogin.lower() in logins_existentes:
                    print("\nEste login já está em uso. Escolha outro.\n")
                    continue
                newSenha = getpass.getpass("Digite uma senha: ")
                confirmarSenha = getpass.getpass("Confirmar senha: ")
                if newSenha == confirmarSenha:
                    newUsuario = {"login": newLogin,
                                "senha": newSenha,
                                "usuario": {"read": [],
                                                "write": [],
                                                "delete": []}}
                    usuarios  .append(newUsuario)
                    with open("users.json", mode="w") as arquivo:
                        json.dump(usuarios, arquivo, indent=4)
                    print("\nUsuário cadastrado com sucesso!\n")
                    break
                else:
                    print("\nAs senhas não coincidem. Tente novamente\n")
                    tentativas += 1

        # Sair
        elif menuInicial == "3":
            print("Obrigada pela visita :) \nAté Breve!\n")
            break

        else:
            print("\nErro! Opção inválida!\n")



    try:
        with open("users.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)  
    except FileNotFoundError:
        dados = [] 

    autentificado = False
    tentativas = 0

    while tentativas <= 5:
        login = input("Login: ")
        senha = input("Senha: ")
        if any(dado["nome"] == login and dado["senha"] == senha for dado in dados):
            print(f"\n Seja Bem-vindo: {login}\n")
            autentificado = True
            break
                                
        else:
            print("\n Login ou Senha incorretos, por favor tente novamente \n")
            tentativas +=1
        
        if tentativas == 5:   
            print("Muitas tentativas! Acesso Bloqueado!")
            break
        elif autentificado == True:
            break