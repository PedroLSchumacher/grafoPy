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
    salvar_e_mostrar_grafo,
    validar_peso,
    verificar_existencia_tarefa,
    verificar_existencia_relacao
)

nome_arquivo_grafo = "meu_grafo.txt"

def menu_usuario():
    grafo_tarefas = carregar_grafo_de_txt(nome_arquivo_grafo)

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
        print("9. Salvar e visualizar grafo")
        print("10. Listar dados do grafo")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            vertice = input("Informe o nome da tarefa a ser adicionada: ")
            adicionar_vertice(grafo_tarefas, vertice)

        elif opcao == "2":
            tarefa1 = input("Informe a primeira tarefa: ")
            tarefa2 = input("Informe a segunda tarefa: ")
            if verificar_existencia_tarefa(grafo_tarefas, tarefa1) and verificar_existencia_tarefa(grafo_tarefas, tarefa2):
                peso = validar_peso()  # Valida o peso entre 0 e 10
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
            salvar_e_mostrar_grafo()

        elif opcao == "10":
            listar_grafo(grafo_tarefas)

        elif opcao == "0":
            salvar_grafo_em_txt(grafo_tarefas, nome_arquivo_grafo)
            print("Grafo salvo. Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Admin")
        print("2. Usuário")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Parabéns, você é um admin.")
            # Admin pode ter funcionalidades extras no futuro

        elif opcao == "2":
            menu_usuario()

        elif opcao == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
