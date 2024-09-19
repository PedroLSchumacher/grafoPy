# main2.py

from functions.functions import Grafo, autenticar, fazer_autenticacao

def main():
    nome, user = autenticar()
    if user:
        fazer_autenticacao(nome, user)
        grafo = Grafo()
        # Adicione mais lógica para usar o objeto 'grafo' conforme necessário

if __name__ == "__main__":
    main()
