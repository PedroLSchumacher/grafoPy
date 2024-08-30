import networkx as nx
import matplotlib.pyplot as plt
import re

def validar_entrada(texto):
    if texto and not re.match("^[A-Za-z0-9]+$", texto):
        print("Entrada inválida! Por favor, insira apenas letras.")
        return False
    return True

def criar_grafo():
    G = nx.Graph()
    
    print("Insira os elementos (um por vez). Quando terminar, digite 'sair'.")
    while True:
        no = input("Digite um elemento (ou digite 'sair' para terminar): ").strip().upper()
        if no == "SAIR":
            break
        if validar_entrada(no):
            G.add_node(no)
    
    print("\nInsira as conexões (arestas) entre os elementos. Exemplo: PA C")
    print("Quando terminar, digite 'sair'.")
    while True:
        aresta = input("Digite uma conexão (ou digite 'sair' para terminar): ").strip().upper()
        if aresta == "SAIR":
            break
        try:
            u, v = aresta.split()
            if validar_entrada(u) and validar_entrada(v):
                if u in G.nodes and v in G.nodes:
                    G.add_edge(u, v)
                    
                    # Verificar se formou um subgrafo
                    if len(G.nodes) == 2 and len(G.edges) == 1:
                        print("Um subgrafo foi formado com 2 nós e 1 aresta!")
                else:
                    print("Um ou ambos os elementos não existem. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar dois elementos separados por espaço.")
    
    return G

def mostrar_graus(G):
    graus = dict(G.degree())
    print("\nGrau de cada elemento:")
    for no, grau in graus.items():
        print(f"Elemento {no}: Grau {grau}")

def perguntar_caminho(G):
    print(f"\Elementos disponíveis: {', '.join(G.nodes)}")
    
    partida = input("Informe o local de partida: ").strip().upper()
    while not validar_entrada(partida):
        partida = input("Informe o local de partida: ").strip().upper()

    chegada = input("Informe o local de chegada: ").strip().upper()
    while not validar_entrada(chegada):
        chegada = input("Informe o local de chegada: ").strip().upper()

    if partida not in G.nodes or chegada not in G.nodes:
        print("Local inexistente. Por favor, tente novamente.")
        return perguntar_caminho(G)
    
    return partida, chegada

def calcular_melhor_rota(G, partida, chegada):
    try:
        caminho = nx.shortest_path(G, source=partida, target=chegada)
        return caminho
    except nx.NetworkXNoPath:
        return None

def visualizar_grafo(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=16, font_weight='bold')
    plt.show()

def main():
    G = criar_grafo()
    visualizar_grafo(G)
    
    mostrar_graus(G)  # Mostrar o grau de cada nó

    partida, chegada = perguntar_caminho(G)
    melhor_rota = calcular_melhor_rota(G, partida, chegada)
    
    if melhor_rota:
        print(f"O melhor caminho de {partida} até {chegada} é: {' -> '.join(melhor_rota)}")
    else:
        print(f"Não existe caminho entre {partida} e {chegada}.")

if __name__ == "__main__":
    main()
