# Definindo um dicionário para armazenar informações dos alunos
alunos = {}

# Função para adicionar um novo aluno
def adicionar_aluno():
    nome = input("Digite o nome do novo aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    serie = int(input("Digite a série do aluno: "))
    notas = []
    num_notas = int(input("Quantas notas deseja adicionar? "))
    for i in range(num_notas):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    
    alunos[nome.lower()] = {'nome': nome, 'idade': idade, 'serie': serie, 'notas': notas}
    print(f"Aluno {nome} adicionado com sucesso!")

# Função para exibir informações de um aluno
def exibir_informacoes(aluno):
    print('Nome:', aluno['nome'])
    print('Idade:', aluno['idade'])
    print('Série:', aluno['serie'])
    print('Notas:', aluno['notas'])
    media = sum(aluno['notas']) / len(aluno['notas'])
    print('Média das notas:', media)

while True:
    print("\nOpções:")
    print("1 - Adicionar novo aluno")
    print("2 - Exibir informações de um aluno")
    print("3 - Sair")
    
    opcao = int(input("Digite o número da opção desejada: "))
    
    if opcao == 1:
        adicionar_aluno()
    elif opcao == 2:
        aluno_escolhido = input("Digite o nome do aluno que deseja ver as informações: ").lower()
        if aluno_escolhido in alunos:
            exibir_informacoes(alunos[aluno_escolhido])
        else:
            print('Aluno não encontrado.')
    elif opcao == 3:
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Digite um número válido.")
