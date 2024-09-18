
from functions.functions import autenticar, fazer_autenticacao

def main():
    nome, user = autenticar()

    if user:
        fazer_autenticacao(nome, user)
    else:
        print("Saindo do sistema. Até mais!")

if __name__ == "__main__":
    main()