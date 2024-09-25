import networkx as nx  # Importa a biblioteca networkx para manipulação de grafos
import json  # Importa a biblioteca json para manipulação de arquivos JSON
import os  # Importa a biblioteca os para interações com o sistema operacional

# Função para carregar o grafo de um arquivo .txt
def carregar_grafo_de_txt(nome_arquivo):  
    if os.path.exists(nome_arquivo):  # Verifica se o arquivo existe
        with open(nome_arquivo, "r") as f:  # Abre o arquivo para leitura
            try:
                data = f.read().strip()  # Lê o conteúdo do arquivo e remove espaços em branco
                if data:
                    return nx.node_link_graph(json.loads(data))  # Converte JSON para grafo
                else:
                    print("O arquivo de grafo está vazio. Inicializando com grafo vazio.")
                    return nx.DiGraph()  # Inicializa um grafo direcionado vazio
            except json.JSONDecodeError:
                print("Erro ao carregar o grafo. O arquivo não contém um JSON válido.")
                return nx.DiGraph()  # Retorna um grafo vazio em caso de erro de decodificação
    else:
        print(f"O arquivo {nome_arquivo} não existe. Criando um grafo vazio.")
        return nx.DiGraph()  # Retorna um grafo vazio se o arquivo não existir

# Função para salvar o grafo em um arquivo .txt
def salvar_grafo_em_txt(grafo, nome_arquivo):  
    with open(nome_arquivo, "w") as f:  # Abre o arquivo para escrita
        json.dump(nx.node_link_data(grafo), f)  # Converte o grafo para JSON e escreve no arquivo

# Função para validar o peso entre 0 e 3
def validar_peso():
    while True:
        try:
            peso = int(input("De 0 a 3, o quão você gostaria de realizar esta tarefa?... "))  # Solicita entrada do usuário
            if 0 <= peso <= 3:  # Verifica se o peso está no intervalo válido
                return peso  # Retorna o peso válido
            else:
                print("Peso inválido. Informe um valor entre 0 e 3.")
        except ValueError:
            print("Entrada inválida. Informe um número entre 0 e 3.")  # Exibe mensagem de erro em caso de valor inválido

# Verificar se uma tarefa existe
def verificar_existencia_tarefa(grafo, tarefa):
    if grafo.has_node(tarefa):  # Verifica se o nó (tarefa) existe no grafo
        return True  # Retorna True se a tarefa existe
    else:
        return False  # Retorna False se a tarefa não existe

# Verificar se uma relação existe
def verificar_existencia_relacao(grafo, tarefa1, tarefa2):
    if grafo.has_edge(tarefa1, tarefa2):  # Verifica se a aresta (relação) entre as tarefas existe
        return True  # Retorna True se a relação existe
    else:
        print(f"Relação entre '{tarefa1}' e '{tarefa2}' não existe.")
        return False  # Retorna False se a relação não existe

# Adicionar vértice (tarefa)
def adicionar_vertice(grafo, vertice):
    if not grafo.has_node(vertice):  # Verifica se o vértice não existe no grafo
        grafo.add_node(vertice)  # Adiciona o vértice ao grafo
        print(f"Tarefa '{vertice}' adicionada com sucesso.")
    else:
        print(f"Tarefa '{vertice}' já existe.")

# Adicionar aresta (relação)
def adicionar_aresta(grafo, tarefa1, tarefa2, peso):
    if tarefa1 in grafo and tarefa2 in grafo:  # Verifica se ambas as tarefas existem no grafo
        if tarefa1 != tarefa2:
            grafo.add_edge(tarefa1, tarefa2, weight=peso)  # Adiciona aresta com o peso entre as tarefas
            print(f"Relação entre '{tarefa1}' e '{tarefa2}' adicionada com sucesso com peso {peso}.")
        else:
            print("Uma tarefa não pode se relacionar com ela mesma.")
    else:
        print("Ambas as tarefas precisam estar cadastradas.")

# Consultar vértice (tarefa)
def consultar_vertice(grafo, vertice):
    if grafo.has_node(vertice):  # Verifica se o vértice existe no grafo
        adjacencias = list(grafo[vertice])  # Obtém as tarefas adjacentes (relacionadas)
        if adjacencias:
            print(f"A tarefa '{vertice}' tem relações com: {adjacencias}")
            for adj in adjacencias:
                peso = grafo[vertice][adj]['weight']  # Obtém o peso da relação
                print(f"Peso da relação com '{adj}': {peso}")
        else:
            print(f"A tarefa '{vertice}' não tem relações com outras tarefas.")
    else:
        print(f"Tarefa '{vertice}' não encontrada.")

# Consultar aresta (relação)
def consultar_aresta(grafo, tarefa1, tarefa2):
    if grafo.has_edge(tarefa1, tarefa2):  # Verifica se a aresta existe
        peso = grafo[tarefa1][tarefa2]['weight']  # Obtém o peso da aresta
        print(f"A relação entre '{tarefa1}' e '{tarefa2}' existe com peso {peso}.")
    else:
        print(f"A relação entre '{tarefa1}' e '{tarefa2}' não existe.")

# Remover vértice (tarefa)
def remover_vertice(grafo, vertice):
    if grafo.has_node(vertice):  # Verifica se o vértice existe
        grafo.remove_node(vertice)  # Remove o vértice
        print(f"Tarefa '{vertice}' removida com sucesso.")
    else:
        print(f"Tarefa '{vertice}' não encontrada.")

# Remover aresta (relação)
def remover_aresta(grafo, tarefa1, tarefa2):
    if grafo.has_edge(tarefa1, tarefa2):  # Verifica se a aresta existe
        grafo.remove_edge(tarefa1, tarefa2)  # Remove a aresta
        print(f"Relação entre '{tarefa1}' e '{tarefa2}' removida com sucesso.")
    else:
        print(f"A relação entre '{tarefa1}' e '{tarefa2}' não existe.")

# Atualizar vértice (tarefa)
