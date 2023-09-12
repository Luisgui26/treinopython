aluno = {}

aluno['nome'] = input('Informe o nome do aluno: ')
aluno['media'] = int(input('INforme a média do aluno: '))
if aluno['media'] >= 6:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} = {v}')