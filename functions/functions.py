import networkx as nx
import json
import os

# Função para carregar o grafo de um arquivo .txt
def carregar_grafo_de_txt(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r") as f:
            try:
                data = f.read().strip()
                if data:
                    return nx.node_link_graph(json.loads(data))
                else:
                    print("O arquivo de grafo está vazio. Inicializando com grafo vazio.")
                    return nx.DiGraph()  # Inicializa grafo vazio
            except json.JSONDecodeError:
                print("Erro ao carregar o grafo. O arquivo não contém um JSON válido.")
                return nx.DiGraph()  # Retorna um grafo vazio em caso de erro
    else:
        print(f"O arquivo {nome_arquivo} não existe. Criando um grafo vazio.")
        return nx.DiGraph()

# Função para salvar o grafo em um arquivo .txt
def salvar_grafo_em_txt(grafo, nome_arquivo):
    with open(nome_arquivo, "w") as f:
        json.dump(nx.node_link_data(grafo), f)

# Função para validar o peso entre 0 e 10
def validar_peso():
    while True:
        try:
            peso = int(input("De 0 a 10, o quão gostaria de executar esta relação? "))
            if 0 <= peso <= 10:
                return peso
            else:
                print("Peso inválido. Informe um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Informe um número entre 0 e 10.")

# Verificar se uma tarefa existe
def verificar_existencia_tarefa(grafo, tarefa):
    if grafo.has_node(tarefa):
        return True
    else:
        print(f"Tarefa '{tarefa}' não existe.")
        return False

# Verificar se uma relação existe
def verificar_existencia_relacao(grafo, tarefa1, tarefa2):
    if grafo.has_edge(tarefa1, tarefa2):
        return True
    else:
        print(f"Relação entre '{tarefa1}' e '{tarefa2}' não existe.")
        return False

# Adicionar vértice (tarefa)
def adicionar_vertice(grafo, vertice):
    if not grafo.has_node(vertice):
        grafo.add_node(vertice)
        print(f"Tarefa '{vertice}' adicionada com sucesso.")
    else:
        print(f"Tarefa '{vertice}' já existe.")

# Adicionar aresta (relação)
def adicionar_aresta(grafo, tarefa1, tarefa2, peso):
    if tarefa1 in grafo and tarefa2 in grafo:
        if tarefa1 != tarefa2:
            grafo.add_edge(tarefa1, tarefa2, weight=peso)
            print(f"Relação entre '{tarefa1}' e '{tarefa2}' adicionada com sucesso com peso {peso}.")
        else:
            print("Uma tarefa não pode se relacionar com ela mesma.")
    else:
        print("Ambas as tarefas precisam estar cadastradas.")

# Consultar vértice (tarefa)
def consultar_vertice(grafo, vertice):
    if grafo.has_node(vertice):
        adjacencias = list(grafo[vertice])
        if adjacencias:
            print(f"A tarefa '{vertice}' tem relações com: {adjacencias}")
            for adj in adjacencias:
                print(f"- Relacionado com '{adj}' com peso {grafo[vertice][adj]['weight']}")
        else:
            print(f"A tarefa '{vertice}' não tem relações.")
    else:
        print(f"Tarefa '{vertice}' não existe.")

# Consultar aresta (relação)
def consultar_aresta(grafo, tarefa1, tarefa2):
    if grafo.has_edge(tarefa1, tarefa2):
        peso = grafo[tarefa1][tarefa2]['weight']
        print(f"A relação entre '{tarefa1}' e '{tarefa2}' existe com peso {peso}.")
    else:
        print(f"Relação entre '{tarefa1}' e '{tarefa2}' não foi encontrada.")

# Remover vértice (tarefa)
def remover_vertice(grafo, vertice):
    if grafo.has_node(vertice):
        grafo.remove_node(vertice)
        print(f"Tarefa '{vertice}' removida com sucesso.")
    else:
        print(f"Tarefa '{vertice}' não existe.")

# Remover aresta (relação)
def remover_aresta(grafo, tarefa1, tarefa2):
    if grafo.has_edge(tarefa1, tarefa2):
        grafo.remove_edge(tarefa1, tarefa2)
        print(f"Relação entre '{tarefa1}' e '{tarefa2}' removida com sucesso.")
    else:
        print(f"Relação entre '{tarefa1}' e '{tarefa2}' não existe.")

# Atualizar vértice (nome da tarefa)
def atualizar_vertice(grafo, vertice_antigo, vertice_novo):
    if grafo.has_node(vertice_antigo):
        nx.relabel_nodes(grafo, {vertice_antigo: vertice_novo}, copy=False)
        print(f"Tarefa '{vertice_antigo}' atualizada para '{vertice_novo}'.")
    else:
        print(f"Tarefa '{vertice_antigo}' não existe.")

# Atualizar aresta (relação)
def atualizar_aresta(grafo, tarefa1, tarefa2, novo_peso):
    if grafo.has_edge(tarefa1, tarefa2):
        grafo[tarefa1][tarefa2]['weight'] = novo_peso
        print(f"Peso da relação entre '{tarefa1}' e '{tarefa2}' atualizado para {novo_peso}.")
    else:
        print(f"Relação entre '{tarefa1}' e '{tarefa2}' não foi encontrada.")

# Listar dados do grafo
def listar_grafo(grafo):
    print("Tarefas no grafo: ", list(grafo.nodes))
    print("Relações no grafo: ", list(grafo.edges(data=True)))

    # Verifica se o grafo é um dígrafo (direcionado) ou grafo (não direcionado)
    if isinstance(grafo, nx.DiGraph):
        print("O grafo é um dígrafo (direcionado).")
    else:
        print("O grafo é um grafo (não direcionado).")

    # Verifica se o grafo é valorado ou não
    valorado = any('weight' in grafo[edge[0]][edge[1]] for edge in grafo.edges)
    if valorado:
        print("O grafo é valorado (tem pesos).")
    else:
        print("O grafo não é valorado (não tem pesos).")

    # Verifica se o grafo tem laços (vértices com relações a eles mesmos)
    tem_laco = any(grafo.has_edge(node, node) for node in grafo.nodes)
    if tem_laco:
        print("O grafo tem laços.")
    else:
        print("O grafo não tem laços.")

    # Exibir o grau de cada tarefa
    for node in grafo.nodes:
        print(f"O grau da tarefa '{node}' é {grafo.degree[node]}.")

# Salvar e mostrar grafo
def salvar_e_mostrar_grafo():
    print("Grafo salvo e mostrado com sucesso.")
