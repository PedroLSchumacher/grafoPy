# functions/grafo_functions.py

def imprimir_menu():
    print("=-=-=-=-= > MENU DE AUTENTICAÇÃO < =-=-=-=-=")
    print("1 - Admin")
    print("2 - Usuario")
    print("3 - Sair")

def autenticar():
    nome = input("Por favor, insira seu nome: ")

    while True:
        imprimir_menu()
        escolha = input(f"Olá, {nome}. Escolha uma das opções (1, 2 ou 3): ")

        if escolha == '1':
            return nome, "admin"
        elif escolha == '2':
            return nome, "usuario"
        elif escolha == '3':
            print("Saindo do sistema. Até mais!")
            return None, None
        else:
            print("Opção inválida. Tente novamente.")

def fazer_autenticacao(nome, user):
    if user == "admin":
        print("Bem-vindo, Admin!")
    elif user == "usuario":
        print(f"Seja bem-vindo, {nome}!")
    else:
        print("Tipo de usuário não reconhecido.")

class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz_adjacencia = []

    def carregar_grafo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
                num_vertices = int(linhas[0].strip())
                self.vertices = []
                self.matriz_adjacencia = [[0] * num_vertices for _ in range(num_vertices)]
                
                for linha in linhas[1:]:
                    v1, v2, valor = linha.strip().split()
                    valor = int(valor)
                    self.adicionar_vertice(v1)
                    self.adicionar_vertice(v2)
                    self.adicionar_aresta(v1, v2, valor)
        except FileNotFoundError:
            print(f"Arquivo {nome_arquivo} não encontrado.")

    def salvar_grafo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(f"{len(self.vertices)}\n")
            for i in range(len(self.vertices)):
                for j in range(i, len(self.vertices)):
                    if self.matriz_adjacencia[i][j] != 0:
                        arquivo.write(f"{self.vertices[i]} {self.vertices[j]} {self.matriz_adjacencia[i][j]}\n")

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices.append(vertice)
            for linha in self.matriz_adjacencia:
                linha.append(0)
            self.matriz_adjacencia.append([0] * len(self.vertices))
            print(f"Vértice {vertice} adicionado.")
        else:
            print(f"Vértice {vertice} já existe.")

    def adicionar_aresta(self, vertice1, vertice2, valor):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            indice1 = self.vertices.index(vertice1)
            indice2 = self.vertices.index(vertice2)
            self.matriz_adjacencia[indice1][indice2] = valor
            self.matriz_adjacencia[indice2][indice1] = valor  # Para grafos não direcionados
            print(f"Aresta entre {vertice1} e {vertice2} com valor {valor} adicionada.")
        else:
            print("Um ou ambos os vértices não foram encontrados.")

    def consultar_vertice(self, vertice):
        if vertice in self.vertices:
            print(f"Vértice {vertice} existe no grafo.")
        else:
            print(f"Vértice {vertice} não encontrado.")

    def consultar_aresta(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            indice1 = self.vertices.index(vertice1)
            indice2 = self.vertices.index(vertice2)
            valor = self.matriz_adjacencia[indice1][indice2]
            if valor != 0:
                print(f"Aresta entre {vertice1} e {vertice2} tem valor {valor}.")
            else:
                print(f"Não há aresta entre {vertice1} e {vertice2}.")
        else:
            print("Um ou ambos os vértices não foram encontrados.")

    def remover_vertice(self, vertice):
        if vertice in self.vertices:
            indice = self.vertices.index(vertice)
            self.vertices.pop(indice)
            self.matriz_adjacencia.pop(indice)
            for linha in self.matriz_adjacencia:
                linha.pop(indice)
            print(f"Vértice {vertice} removido.")
        else:
            print(f"Vértice {vertice} não encontrado.")

    def remover_aresta(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            indice1 = self.vertices.index(vertice1)
            indice2 = self.vertices.index(vertice2)
            self.matriz_adjacencia[indice1][indice2] = 0
            self.matriz_adjacencia[indice2][indice1] = 0  # Para grafos não direcionados
            print(f"Aresta entre {vertice1} e {vertice2} removida.")
        else:
            print("Um ou ambos os vértices não foram encontrados.")

    def atualizar_vertice(self, vertice_antigo, vertice_novo):
        if vertice_antigo in self.vertices:
            indice = self.vertices.index(vertice_antigo)
            self.vertices[indice] = vertice_novo
            print(f"Vértice {vertice_antigo} atualizado para {vertice_novo}.")
        else:
            print(f"Vértice {vertice_antigo} não encontrado.")

    def atualizar_aresta(self, vertice1, vertice2, novo_valor):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            indice1 = self.vertices.index(vertice1)
            indice2 = self.vertices.index(vertice2)
            self.matriz_adjacencia[indice1][indice2] = novo_valor
            self.matriz_adjacencia[indice2][indice1] = novo_valor  # Para grafos não direcionados
            print(f"Aresta entre {vertice1} e {vertice2} atualizada para {novo_valor}.")
        else:
            print("Um ou ambos os vértices não foram encontrados.")

    def listar_dados_grafo(self):
        print(f"Vértices: {self.vertices}")
        print("Matriz de Adjacência:")
        for linha in self.matriz_adjacencia:
            print(linha)
