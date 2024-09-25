import networkx as nx
from functions.functions import (
    carregar_grafo_de_txt,
    salvar_grafo_em_txt,
    adicionar_vertice,
    adicionar_aresta,
    consultar_vertice,
    consultar_aresta,
    remover_vertice,
    remover_aresta,
    atualizar_vertice,
    atualizar_aresta,
    listar_grafo,
    validar_peso,
    verificar_existencia_tarefa,
    verificar_existencia_relacao,
    sugerir_proxima_tarefa,
    zerar_grafo
)

nome_arquivo_grafo = "meu_grafo.txt"

def menu_usuario():
    grafo_tarefas = carregar_grafo_de_txt(nome_arquivo_grafo)

    # Menu para escolher entre sugestão de próxima atividade ou editar a rotina
    print("\n=== O QUE VOCÊ DESEJA FAZER? ===")
    print("1. Sugestão de próxima atividade")
    print("2. Editar rotina - Menu de Tarefas")
    opcao_usuario = input("Escolha uma opção: ")

    if opcao_usuario == "1":  # Seguir com sugestão de próxima atividade
            ultima_atividade = input("Qual foi sua última atividade? ")
            
            if verificar_existencia_tarefa(grafo_tarefas, ultima_atividade):
                estado_usuario = input("Como você está? (1: Estou bem; 2: Estou mais ou menos; 3: Estou cansado): ")
                if estado_usuario in ['1', '2', '3']:
                    relacionamentos = list(grafo_tarefas.neighbors(ultima_atividade))
                    
                    if relacionamentos:
                        sugerir_proxima_tarefa(grafo_tarefas, estado_usuario, ultima_atividade)
                    else:
                        print("Não há tarefas relacionadas a sua última atividade.")
            else:
                print(f"Sua última atividade '{ultima_atividade}' não está registrada na sua rotina.")
                proxima_atividade = input("Qual seria sua próxima atividade agora (digite o nome da tarefa): ")
                if verificar_existencia_tarefa(grafo_tarefas, proxima_atividade):
                    estado_usuario = input("Como você está? (1: Estou bem; 2: Estou mais ou menos; 3: Estou cansado): ")
                    if estado_usuario in ['1', '2', '3']:
                        sugerir_proxima_tarefa(grafo_tarefas, estado_usuario, proxima_atividade)
                else:
                    print(f"A tarefa '{proxima_atividade}' não existe na sua rotina ainda, mas se quiser, pode adicionar ela abaixo e informar sua relação com outras atividades.")
        
    elif opcao_usuario == "2":  # Abrir o menu de edição de rotina (Menu de Tarefas)
            while True:
                print("\n=== MENU DE TAREFAS ===")
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
                    vertice = input("Informe o nome da tarefa a ser adicionada: ")
                    adicionar_vertice(grafo_tarefas, vertice)

                elif opcao == "2":
                    tarefa1 = input("Informe a primeira tarefa: ")
                    tarefa2 = input("Informe a segunda tarefa: ")
                    if verificar_existencia_tarefa(grafo_tarefas, tarefa1) and verificar_existencia_tarefa(grafo_tarefas, tarefa2):
                        peso = validar_peso()
                        adicionar_aresta(grafo_tarefas, tarefa1, tarefa2, peso)

                elif opcao == "3":
                    vertice = input("Informe o nome da tarefa para consulta: ")
                    if verificar_existencia_tarefa(grafo_tarefas, vertice):
                        consultar_vertice(grafo_tarefas, vertice)

                elif opcao == "4":
                    tarefa1 = input("Informe a primeira tarefa: ")
                    tarefa2 = input("Informe a segunda tarefa: ")
                    if verificar_existencia_relacao(grafo_tarefas, tarefa1, tarefa2):
                        consultar_aresta(grafo_tarefas, tarefa1, tarefa2)

                elif opcao == "5":
                    vertice = input("Informe a tarefa a ser removida: ")
                    if verificar_existencia_tarefa(grafo_tarefas, vertice):
                        remover_vertice(grafo_tarefas, vertice)

                elif opcao == "6":
                    tarefa1 = input("Informe a primeira tarefa: ")
                    tarefa2 = input("Informe a segunda tarefa: ")
                    if verificar_existencia_relacao(grafo_tarefas, tarefa1, tarefa2):
                        remover_aresta(grafo_tarefas, tarefa1, tarefa2)

                elif opcao == "7":
                    vertice_antigo = input("Informe o nome da tarefa atual: ")
                    vertice_novo = input("Informe o novo nome da tarefa: ")
                    if verificar_existencia_tarefa(grafo_tarefas, vertice_antigo):
                        atualizar_vertice(grafo_tarefas, vertice_antigo, vertice_novo)

                elif opcao == "8":
                    tarefa1 = input("Informe a primeira tarefa: ")
                    tarefa2 = input("Informe a segunda tarefa: ")
                    if verificar_existencia_relacao(grafo_tarefas, tarefa1, tarefa2):
                        novo_peso = validar_peso()
                        atualizar_aresta(grafo_tarefas, tarefa1, tarefa2, novo_peso)

                elif opcao == "9":
                    listar_grafo(grafo_tarefas)

                elif opcao == "10":  # Listar todas as tarefas
                    if grafo_tarefas.number_of_nodes() > 0:
                        print("=== Tarefas ===")
                        for tarefa in grafo_tarefas.nodes:
                            print(f"- {tarefa}")
                    else:
                        print("Não há tarefas cadastradas.")

                elif opcao == "11":  # Listar todas as relações
                    if grafo_tarefas.number_of_edges() > 0:
                        print("=== Relações ===")
                        for tarefa1, tarefa2, peso in grafo_tarefas.edges(data='weight'):
                            print(f"{tarefa1} -> {tarefa2} (Peso: {peso})")
                    else:
                        if grafo_tarefas.number_of_nodes() > 0:
                            print("Não há relações, apenas tarefas cadastradas.")
                        else:
                            print("Não há tarefas ou relações cadastradas.")

                elif opcao == "0":
                    salvar_grafo_em_txt(grafo_tarefas, nome_arquivo_grafo)
                    print("Tarefa salva. Encerrando o programa...")
                    break

                else:
                    print("Opção inválida. Tente novamente.")

def menu_principal():
    nome_arquivo = "meu_grafo.txt"  # Defina o nome do seu arquivo aqui
    grafo = carregar_grafo_de_txt(nome_arquivo)

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Admin")
        print("2. Usuário")
        print("3. Apagar rotina")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Parabéns, você é um admin.")
            # Admin pode ter funcionalidades extras no futuro

        elif opcao == "2":
            menu_usuario()

        elif opcao == "3":
            zerar_grafo(nome_arquivo)
            grafo = nx.DiGraph()
            print("Sua rotina está vazia.")

        elif opcao == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
