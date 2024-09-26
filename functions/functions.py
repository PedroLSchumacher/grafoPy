import networkx as nx  # Importa a biblioteca networkx para manipulação de grafos
import json  # Importa a biblioteca json para manipulação de arquivos JSON
import os  # Importa a biblioteca os para interações com o sistema operacional

# Função para carregar o grafo de um arquivo .txt
def carregar_grafo_de_txt(matriz):  
    if os.path.exists(matriz):  # Verifica se o arquivo existe
        with open(matriz, "r") as f:  # Abre o arquivo para leitura
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
        print(f"O arquivo {matriz} não existe. Criando um grafo vazio.")
        return nx.DiGraph()  # Retorna um grafo vazio se o arquivo não existir

# Função para salvar o grafo em um arquivo .txt
def salvar_grafo_em_txt(grafo, matriz):  
    with open(matriz, "w") as f:  # Abre o arquivo para escrita
        json.dump(nx.node_link_data(grafo), f)  # Converte o grafo para JSON e escreve no arquivo

# Função para validar o peso entre 0 e 3
def validar_peso():
    while True:
        try:
            peso = int(input("De 1 a 3, o quão você gostaria de realizar esta tarefa após a outra?... Lembrando, 1 = Estou bem, posso realizar | 2 = Estou mais ou menos | 3 = Estou mal, melhor relaxar. "))  # Solicita entrada do usuário
            if 1 <= peso <= 3:  # Verifica se o peso está no intervalo válido
                return peso  # Retorna o peso válido
            else:
                print("Peso inválido. Informe um valor de 1 a 3.")
        except ValueError:
            print("Entrada inválida. Informe o valor de 1 a 3.")  # Exibe mensagem de erro em caso de valor inválido

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
def zerar_grafo(matriz):
    with open(matriz, "w") as f:
        f.write("")  # Limpa o conteúdo do arquivo
    print(f"O conteúdo do arquivo '{matriz}' foi apagado.")

