import networkx as nx  # Importa o módulo NetworkX para criar e manipular grafos
from functions.functions import (  # Importa várias funções específicas da biblioteca 'functions'
    carregar_grafo_de_txt,  # Função para carregar um grafo a partir de um arquivo .txt
    salvar_grafo_em_txt,  # Função para salvar um grafo em um arquivo .txt
    adicionar_vertice,  # Função para adicionar um vértice ao grafo
    adicionar_aresta,  # Função para adicionar uma aresta entre dois vértices no grafo
    consultar_vertice,  # Função para consultar informações de um vértice
    consultar_aresta,  # Função para consultar informações de uma aresta
    remover_vertice,  # Função para remover um vértice do grafo
    remover_aresta,  # Função para remover uma aresta entre dois vértices
    atualizar_vertice,  # Função para atualizar informações de um vértice
    atualizar_aresta,  # Função para atualizar informações de uma aresta
    listar_grafo,  # Função para listar todos os vértices e arestas do grafo
    validar_peso,  # Função para validar o peso das arestas
    verificar_existencia_tarefa,  # Função para verificar se uma tarefa (vértice) existe no grafo
    verificar_existencia_relacao,  # Função para verificar se existe uma relação (aresta) entre duas tarefas
    sugerir_proxima_tarefa,  # Função para sugerir a próxima tarefa a ser realizada
    zerar_grafo  # Função para zerar o grafo (remover todas as tarefas e relações)
)

arquivo_grafo = "meu_grafo.txt"  # Define o nome do arquivo onde o grafo será carregado e salvo

def menu_usuario():  # Define a função principal do menu de interação com o usuário
    grafo_tarefas = carregar_grafo_de_txt(arquivo_grafo)  # Carrega o grafo a partir do arquivo de texto

    # Menu para escolher entre sugestão de próxima atividade ou editar a rotina
    print("\n=== O QUE VOCÊ DESEJA FAZER? ===")  # Exibe o título do menu
    print("1. Sugestão de próxima atividade")  # Opção 1: Sugestão de próxima tarefa
    print("2. Editar rotina - Menu de Tarefas")  # Opção 2: Editar a rotina (tarefas e relações)
    opcao_usuario = input("Escolha uma opção: ")  # Solicita ao usuário que escolha uma das opções

    if opcao_usuario == "1":  # Se a opção escolhida for "1" (Sugestão de próxima atividade)
        ultima_atividade = input("Qual foi sua última atividade? ")  # Solicita ao usuário a última atividade realizada
            
        if verificar_existencia_tarefa(grafo_tarefas, ultima_atividade):  # Verifica se a última atividade existe no grafo
            estado_usuario = input("Como você está? (1: Estou bem; 2: Estou mais ou menos; 3: Estou cansado): ")  # Pergunta como o usuário está se sentindo
            if estado_usuario in ['1', '2', '3']:  # Verifica se o estado inserido pelo usuário é válido
                relacionamentos = list(grafo_tarefas.neighbors(ultima_atividade))  # Obtém as tarefas relacionadas à última atividade
                if relacionamentos:  # Se houver tarefas relacionadas
                    sugerir_proxima_tarefa(grafo_tarefas, estado_usuario, ultima_atividade)  # Sugere a próxima tarefa com base no estado e na última atividade
                else:  # Caso não haja tarefas relacionadas
                    print("Não há tarefas relacionadas a sua última atividade.")  # Exibe mensagem informando que não há relacionamentos
        else:  # Se a última atividade não existir no grafo
            print(f"Sua última atividade '{ultima_atividade}' não está registrada na sua rotina.")  # Informa que a atividade não está registrada
            proxima_atividade = input("Qual seria sua próxima atividade agora (digite o nome da tarefa): ")  # Solicita ao usuário a próxima atividade que deseja realizar
            if verificar_existencia_tarefa(grafo_tarefas, proxima_atividade):  # Verifica se a próxima atividade existe no grafo
                estado_usuario = input("Como você está? (1: Estou bem; 2: Estou mais ou menos; 3: Estou cansado): ")  # Pergunta novamente como o usuário está se sentindo
                if estado_usuario in ['1', '2', '3']:  # Verifica se o estado é válido
                    sugerir_proxima_tarefa(grafo_tarefas, estado_usuario, proxima_atividade)  # Sugere a próxima tarefa com base no estado e na atividade informada
            else:  # Se a tarefa ainda não existir no grafo
                print(f"A tarefa '{proxima_atividade}' não existe na sua rotina ainda, mas se quiser, pode adicionar ela abaixo e informar sua relação com outras atividades.")  # Informa que a tarefa não está registrada, mas oferece a opção de adicioná-la
        
    elif opcao_usuario == "2":  # Abrir o menu de edição de rotina (Menu de Tarefas)
            while True:
                print("\n=== MENU DE TAREFAS ===") # Menu que aparece com as funções sugeridas e algumas funções para o usuário. Outras funções estão mais abaixo
                print("1. Adicionar tarefa (vértice)")
                print("2. Adicionar relação entre tarefas (aresta)")
                print("3. Consultar tarefa")
                print("4. Consultar relação")
                print("5. Remover tarefa")
                print("6. Remover relação")
                print("7. Atualizar tarefa")
                print("8. Atualizar relação")
                print("9. Listar dados da rotina")
                print("10. Listar todas as tarefas")
                print("11. Listar todas as relações")
                print("0. Sair para gerar a rotina informada")

                opcao = input("Escolha uma opção: ")

                if opcao == "1":
                    vertice = input("Informe o nome da tarefa a ser adicionada: ") # Solicita ao usuário o nome da tarefa a ser adicionada
                    adicionar_vertice(grafo_tarefas, vertice) # Chama a função para adicionar a tarefa

                elif opcao == "2":
                    tarefa1 = input("Informe a primeira tarefa: ") # Informar a primeira tarefa
                    tarefa2 = input("Informe a segunda tarefa: ") # Informar a segunda tarefa
                    if verificar_existencia_tarefa(grafo_tarefas, tarefa1) and verificar_existencia_tarefa(grafo_tarefas, tarefa2): # Verificar se a tarefa existe
                        peso = validar_peso() # Validar valor da aresta
                        adicionar_aresta(grafo_tarefas, tarefa1, tarefa2, peso)

                elif opcao == "3": # Consultar tarefa
                    vertice = input("Informe o nome da tarefa para consulta: ") 
                    if verificar_existencia_tarefa(grafo_tarefas, vertice): # Verificar se a tarefa existe
                        consultar_vertice(grafo_tarefas, vertice) # Consultar vertice

                elif opcao == "4": # Consultar relação
                    tarefa1 = input("Informe a primeira tarefa: ") # Solicita o nome da primeira tarefa
                    tarefa2 = input("Informe a segunda tarefa: ") # Solicita o nome da segunda tarefa
                    if verificar_existencia_relacao(grafo_tarefas, tarefa1, tarefa2): # Verifica se a relação entre as tarefas existe
                        consultar_aresta(grafo_tarefas, tarefa1, tarefa2) # Chama a função para consultar a relação entre as tarefas


                elif opcao == "5": #
                    vertice = input("Informe a tarefa a ser removida: ") # Solicita o nome da tarefa a ser removida
                    if verificar_existencia_tarefa(grafo_tarefas, vertice): # Verifica se a tarefa existe no grafo
                        remover_vertice(grafo_tarefas, vertice) # Chama a função para remover a tarefa do grafo

                elif opcao == "6":
                    tarefa1 = input("Informe a primeira tarefa: ") # Solicita o nome da primeira tarefa
                    tarefa2 = input("Informe a segunda tarefa: ") # Solicita o nome da segunda tarefa
                    if verificar_existencia_relacao(grafo_tarefas, tarefa1, tarefa2): # Verifica se a relação entre as tarefas existe
                        remover_aresta(grafo_tarefas, tarefa1, tarefa2) # Chama a função para remover a relação do grafo

                elif opcao == "7":
                    vertice_antigo = input("Informe o nome da tarefa atual: ") # Solicita o nome da tarefa a ser atualizada 
                    vertice_novo = input("Informe o novo nome da tarefa: ") # Solicita o novo nome para a tarefa
                    if verificar_existencia_tarefa(grafo_tarefas, vertice_antigo): # Verifica se a tarefa existe no grafo
                        atualizar_vertice(grafo_tarefas, vertice_antigo, vertice_novo) # Chama a função para atualizar o nome da tarefa

                elif opcao == "8":
                    tarefa1 = input("Informe a primeira tarefa: ") # Solicita o nome da primeira tarefa
                    tarefa2 = input("Informe a segunda tarefa: ") # Solicita o nome da segunda tarefa
                    if verificar_existencia_relacao(grafo_tarefas, tarefa1, tarefa2): # Verifica se a relação entre as tarefas existe
                        novo_peso = validar_peso() # Valida e obtém o novo peso para a relação
                        atualizar_aresta(grafo_tarefas, tarefa1, tarefa2, novo_peso) # Chama a função para atualizar a relação entre as tarefas

                elif opcao == "9":
                    listar_grafo(grafo_tarefas) # Chama a função para listar os dados completos do grafo

                elif opcao == "10":  # Listar todas as tarefas
                    if grafo_tarefas.number_of_nodes() > 0: # Verifica se há tarefas (vértices) cadastradas no grafo
                        print("=== Tarefas ===") # Exibe o título da seção de tarefas
                        for tarefa in grafo_tarefas.nodes: # Itera sobre todas as tarefas no grafo
                            print(f"- {tarefa}") # Exibe cada tarefa
                    else:
                        print("Não há tarefas cadastradas.") # Informa que não há tarefas cadastradas

                elif opcao == "11":  # Verifica se a opção escolhida foi "11"
                    if grafo_tarefas.number_of_edges() > 0: # Verifica se há relações (arestas) no grafo
                        print("=== Relações ===") # Exibe o título da seção de relações
                        for tarefa1, tarefa2, peso in grafo_tarefas.edges(data='weight'): # Itera sobre as relações no grafo
                            print(f"{tarefa1} -> {tarefa2} (Peso: {peso})") # Exibe cada relação com o peso correspondente
                    else:
                        if grafo_tarefas.number_of_nodes() > 0: # Verifica se há tarefas cadastradas
                            print("Não há relações, apenas tarefas cadastradas.") # Informa que há tarefas, mas nenhuma relação entre elas
                        else:
                            print("Não há tarefas ou relações cadastradas.") # Informa que não há tarefas nem relações cadastradas

                elif opcao == "0":
                    salvar_grafo_em_txt(grafo_tarefas, arquivo_grafo) # Chama a função para salvar o grafo em um arquivo de texto
                    print("Tarefa salva. Encerrando o programa...") # Informa que o grafo foi salvo e que o programa será encerrado
                    break # Encerra o loop

                else:
                    print("Opção inválida. Tente novamente.") # Informa que a opção é inválida e solicita uma nova tentativa

def menu_principal(): # Define a função para o menu principal
    matriz_grafo = "meu_grafo.txt"  # Defina o nome do seu arquivo aqui
    grafo = carregar_grafo_de_txt(matriz_grafo)

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Admin") # Seleciona a opção Admin (Não muda nada)
        print("2. Usuário") # Seleciona a opção Usuário
        print("3. Apagar rotina") # Seleciona a opção Apagar Rotina
        print("0. Sair") # Sair do programa

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Parabéns, você é um admin.")
            # Admin pode ter funcionalidades extras no futuro. No momento é igual ao usuário

        elif opcao == "2":
            menu_usuario() # Chama o menu

        elif opcao == "3":
            zerar_grafo(matriz_grafo) # Chama a função de zerar grafo
            grafo = nx.DiGraph()
            print("Sua rotina está vazia.")

        elif opcao == "0":
            print("Saindo do programa...") #Sai do programa
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__": # Chama a função para exibir o menu principal e iniciar o programa
    menu_principal()
