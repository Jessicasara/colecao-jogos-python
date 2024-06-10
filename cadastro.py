import os

alunos = []

def cadastrar_aluno():
    os.system('cls')
    print('Cadastre o aluno\n')
    nome_aluno = input('''Digite o nome do aluno ❣ ''')
    idade_aluno = input('''Digite a idade do aluno ❣ ''')
    nota_aluno = input('''Digite a nota do aluno ❣ ''')
    dados_do_aluno = {'nome':nome_aluno, 'idade':idade_aluno, 'nota':nota_aluno}
    alunos.append(dados_do_aluno)


def exibir_alunos():
    os.system('cls')
    print('Lista de alunos\n')
    for aluno in alunos:
        nome_aluno = aluno['nome']
        idade_aluno = aluno['idade']
        nota_aluno = aluno['nota']
        print(f'  \n{nome_aluno}  \n{idade_aluno}   \n{nota_aluno}')



def main():
    while True:
        opcao = input('Você deseja cadastrar um novo aluno? ')
        if opcao == 's':
            cadastrar_aluno()
        elif opcao == 'n':
            exibir_alunos()
            break
        else:
            print('Opção inválida')  
    
if __name__ == '__main__':
    main()