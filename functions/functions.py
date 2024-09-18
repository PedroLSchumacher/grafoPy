def imprimir_menu():
    print("=-=-=-=-= > MENU DE AUTENTICAÇÃO < =-=-=-=-=")
    print("1 - Admin")
    print("2 - Usuario")
    print("3 - Sair")

def autenticar():
    nome = input("Por favor, insira seu nome:")

    while True:
        imprimir_menu()
        escolha = input(f"Olá, {nome}. Escolha uma das opções (1, 2 ou 3): ")

        if escolha == '1':
            return "admin"
        elif escolha == '2':
            return "usuario"
        elif escolha == '3':
            print("Tenten novamente")
            return imprimir_menu()
        else:
            print("Caminho errado meu chapa! NT!")

def fazer_autenticacao(nome, user):
    if user == "admin":
        print("Bem-vindo, Admin!")
    elif user == "usuario":
        print(f"Seja bem-vindo, {nome}!")
    else:
        print("Ainda não rolou meu chapa!")


