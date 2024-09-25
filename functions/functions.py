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

# Função para validar o peso entre 0 e 3
def validar_peso():
    while True:
        try:
            peso = int(input("De 0 a 3, o quão você gostaria de realizar esta tarefa? lembrando que 1 = Estou bem posso fazer, 2 = estou mais ou menos e 3 = estou cansado, melhor relaxar: "))
            if 0 <= peso <= 3:
                return peso
            else:
                print("Peso inválido. Informe um valor entre 0 e 3.")
        except ValueError:
            print("Entrada inválida. Informe um número entre 0 e 3.")

# Verificar se uma tarefa existe
def verificar_existencia_tarefa(grafo, tarefa):
    if grafo.has_node(tarefa):
        return True
    else:
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
                peso = grafo[vertice][adj]['weight']
                print(f"Peso da relação com '{adj}': {peso}")
        else:
            print(f"A tarefa '{vertice}' não tem relações com outras tarefas.")
    else:
        print(f"Tarefa '{vertice}' não encontrada.")

# Consultar aresta (relação)
def consultar_aresta(grafo, tarefa1, tarefa2):
    if grafo.has_edge(tarefa1, tarefa2):
        peso = grafo[tarefa1][tarefa2]['weight']
        print(f"A relação entre '{tarefa1}' e '{tarefa2}' existe com peso {peso}.")
    else:
        print(f"A relação entre '{tarefa1}' e '{tarefa2}' não existe.")

# Remover vértice (tarefa)
def remover_vertice(grafo, vertice):
    if grafo.has_node(vertice):
        grafo.remove_node(vertice)
        print(f"Tarefa '{vertice}' removida com sucesso.")
    else:
        print(f"Tarefa '{vertice}' não encontrada.")

# Remover aresta (relação)
def remover_aresta(grafo, tarefa1, tarefa2):
    if grafo.has_edge(tarefa1, tarefa2):
        grafo.remove_edge(tarefa1, tarefa2)
        print(f"Relação entre '{tarefa1}' e '{tarefa2}' removida com sucesso.")
    else:
        print(f"A relação entre '{tarefa1}' e '{tarefa2}' não existe.")

# Atualizar vértice (tarefa)
def atualizar_vertice(grafo, vertice_antigo, vertice_novo):
    if grafo.has_node(vertice_antigo):
        grafo.add_node(vertice_novo)
        for adj in list(grafo.adjacency()):
            if vertice_antigo in grafo[adj[0]]:
                grafo.add_edge(vertice_novo, adj[0], weight=grafo[adj[0]][vertice_antigo]['weight'])
        grafo.remove_node(vertice_antigo)
        print(f"Tarefa '{vertice_antigo}' atualizada para '{vertice_novo}' com sucesso.")
    else:
        print(f"Tarefa '{vertice_antigo}' não encontrada.")

# Atualizar aresta (relação)
def atualizar_aresta(grafo, tarefa1, tarefa2, novo_peso):
    if grafo.has_edge(tarefa1, tarefa2):
        grafo[tarefa1][tarefa2]['weight'] = novo_peso
        print(f"Peso da relação entre '{tarefa1}' e '{tarefa2}' atualizado para {novo_peso}.")
    else:
        print(f"A relação entre '{tarefa1}' e '{tarefa2}' não existe.")

# Listar dados do grafo
# Função para listar o grafo com informações adicionais
def listar_grafo(grafo):
    # Tipo do grafo: Grafo ou Dígrafo
    tipo_grafo = "Dígrafo" if isinstance(grafo, nx.DiGraph) else "Grafo"
    print(f"Tipo do grafo: {tipo_grafo}")

    # Verificar se o grafo é valorado (tem pesos nas arestas)
    valorado = all('weight' in data for u, v, data in grafo.edges(data=True))
    print(f"Grafo valorado: {'Sim' if valorado else 'Não'}")

    # Listar vértices e graus
    print("\nVértices e graus:")
    for vertice in grafo.nodes():
        grau_entrada = grafo.in_degree(vertice) if isinstance(grafo, nx.DiGraph) else None
        grau_saida = grafo.out_degree(vertice) if isinstance(grafo, nx.DiGraph) else None
        grau_total = grafo.degree(vertice)
        
        if grau_entrada is not None and grau_saida is not None:
            print(f"Tarefa '{vertice}' - Grau de entrada: {grau_entrada}, Grau de saída: {grau_saida}, Grau total: {grau_total}")
        else:
            print(f"Tarefa '{vertice}' - Grau total: {grau_total}")

    # Verificar e listar arestas
    print("\nArestas:")
    for tarefa1, tarefa2, dados in grafo.edges(data=True):
        peso = dados.get('weight', 'Sem peso')
        print(f"Relação entre '{tarefa1}' e '{tarefa2}' com peso: {peso}")
    
    # Verificar a presença de laços (auto-arestas)
    lacos = list(nx.selfloop_edges(grafo))
    if lacos:
        print("\nO grafo contém laços (auto-arestas) nas seguintes tarefas:")
        for tarefa1, tarefa2 in lacos:
            print(f"Laço na tarefa '{tarefa1}'")
    else:
        print("\nO grafo não contém laços (auto-arestas).")


# Função para sugerir a próxima tarefa com base no estado do usuário
def sugerir_proxima_tarefa(grafo, estado_usuario, ultima_atividade):
    tarefas_disponiveis = []

    # Pesos baseados no estado do usuário
    pesos = {
        '1': 1,  # Estou bem, posso fazer
        '2': 2,  # Estou mais ou menos
        '3': 3   # Estou cansado, melhor relaxar
    }

    # Encontrar tarefas que o usuário pode realizar
    for adj in grafo[ultima_atividade]:
        peso = grafo[ultima_atividade][adj]['weight']
        if peso == pesos[estado_usuario]:
            tarefas_disponiveis.append(adj)

    # Sugerir a próxima tarefa
    if tarefas_disponiveis:
        print(f"Sugestão de tarefa: {tarefas_disponiveis[0]} com peso correspondente ao seu estado.")
    else:
        print("Não há tarefas disponíveis para o seu estado atual. Quem sabe você não adiciona mais algumas tarefas e algumas relações para sua rotina ficar mais completa. O que me diz? Caso não queira, digite 0.")


# Função para zerar o grafo (apagar o arquivo .txt)
def zerar_grafo(nome_arquivo):
    with open(nome_arquivo, "w") as f:
        f.write("")  # Limpa o conteúdo do arquivo
    print(f"O conteúdo do arquivo '{nome_arquivo}' foi apagado.")

