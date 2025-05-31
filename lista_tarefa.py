lista_de_tarefas = []
continuar = True

print("Bem-vinde à sua Lista de Tarefas!")

"""Adiciona nova tarefa"""
def adicionar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.append(tarefa)
    print("--> Tarefa adicionada com sucesso!")
    return lista_de_tarefas

"""Exibe a lista"""
def lista_tarefas(lista_de_tarefas):
    print("\n")
    print(f"{' '*20}lista de Tarefas")
    print("-"*50)
    n = 1
    for tarefa in lista_de_tarefas:
            print(f"{n} - {tarefa}")
            n += 1
    print("\n")
    print("-"*50)

"""Deleta uma tarefa"""
def deletar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.pop((tarefa - 1))
    return lista_de_tarefas

"""Exibe o menu"""
def exibir_menu():
    print("-"*50)
    print("Escolha uma opção: \n" \
    "1 - Inserir uma nova tarefa \n" \
    "2 - Listar tarefas \n" \
    "3 - Deletar tarefa \n" \
    "4 - Sair"
    )
    print("-"*50)

while continuar:
    exibir_menu()
    opcao = input("Insira o que deseja fazer: ")

    if opcao == "1":
        tarefa = input("Insira uma nova tarefa: ")
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)

    elif opcao == "2":
        lista_tarefas(lista_de_tarefas)

    elif opcao == "3":
        tarefa = input("Insira o número da tarefa que deseja deletar: ")
        if not tarefa.isnumeric():
            print("Número inválido!")
        else:
            tarefa = int(tarefa)
            if tarefa > len(lista_de_tarefas) or tarefa <= 0:
                print("Número inválido!")
            else:
                deletar_tarefa(lista_de_tarefas, tarefa)
                print("--> Tarefa deletada com sucesso!")

    elif opcao =="4":
        continuar = False
        
    else:
        print("opção inválida!")
    print("\n")
