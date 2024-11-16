tarefas = []

def inicia_programa(tarefas):
    #funcao recebe a lista de tarefas como parametro e inicia o programa
    opcao_usuario = entrar_opcao()

    while (opcao_usuario != 5):
        match(opcao_usuario):
            case 1: adicionar_tarefa(tarefas)
            case 2: listar_tarefas(tarefas)
            case 3: marcar_concluida(tarefas)
            case 4: remover_tarefa(tarefas)
            case _: 
                print('---------------------')
                print('opcao inválida!')
        opcao_usuario = entrar_opcao()

def entrar_opcao():
    #funcao que tem o objetivo de apresentar o menu de opcoes para o usuário e retornar qual foi a escolhida
    print('---------------------')
    print('[1] Adicionar Tarefa')
    print('[2] Listar Tarefas')
    print('[3] Marcar Tarefa como Concluída')
    print('[4] Remover Tarefa')
    print('[5] Sair')
    opcao_usuario = int(input("Digite a opção desejada: "))
    return opcao_usuario

def pesquisar_id(id, tarefas):
    #funcao que tem o objetivo de verificar se uma determinada id existe na lista de tarefas ou nao, retorna um booleano de acordo com o resultado do for
    achou = False
    for tarefa in tarefas:
        if (id == tarefa[0]):
            achou = True
            break
    return achou    


def adicionar_tarefa(tarefas):
    #funcao que tem o objetivo de receber do o usuário os metadados da tarefa e adicionar a mesma dentro da lista
    id = int(input('Digite o id da tarefa: '))
    achou = pesquisar_id(id, tarefas)
    if (achou):
        print('---------------------')
        print('Erro: id da tarefa já existe')
        return
    descricao = input('Digite a descricao da tarefa: ')
    status = input('Digite o status da tarefa: ')

    tarefa = [id, descricao, status]
    tarefas.append(tarefa)
    print('---------------------')
    print('Tarefa adicionada com sucesso!')

def listar_tarefas(tarefas):
    #funcao recebe como parametro a lista de tarefas e exibe ela, enumerando-as
    print('---------------------')
    for indice, tarefa in enumerate(tarefas, start=1):
        print(f'{indice}: {tarefa}')  

def marcar_concluida(tarefas):
    #funcao recebe do usuario uma id, verifica se ela existe e marca o status como concluída
    id_escolhido = int(input('Digite o id da tarefa que deseja marcar como concluída: '))
    achou = pesquisar_id(id_escolhido, tarefas)
    if (not achou):
        print('---------------------')
        print('Erro: id inexistente!')
        return
    for tarefa in tarefas:
        if (id_escolhido == tarefa[0]):
            tarefa[2] = 'concluída'
            print('---------------------')
            print('Tarefa marcada como concluída com sucesso!')
            break    

def remover_tarefa(tarefas):
    #funcao recebe do usuario uma id, verifica se ela existe e remove a mesma da lista de tarefas
    id_escolhido = int(input('Digite o id da tarefa que deseja remover: '))
    achou = pesquisar_id(id_escolhido, tarefas)
    if (not achou):
        print('---------------------')
        print('Erro: id inexistente!')
        return
    for tarefa in tarefas:
        if (id_escolhido == tarefa[0]):
            tarefas.remove(tarefa)
            print('---------------------')
            print('Tarefa removida com sucesso!')
            break

inicia_programa(tarefas)        


