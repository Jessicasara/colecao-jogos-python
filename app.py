import os

jogos = [{'nome':'Zelda', 'categoria':'RPG', 'Ativo':False},
         {'nome':'Mario', 'categoria':'Plataforma', 'Ativo':True},
         {'nome':'Metroid', 'categoria':'Plataforma', 'Ativo':True} ]

def exibir_nome_do_programa():
    print('''
    𝕮𝖔𝖑𝖊𝖈̧𝖆̃𝖔 𝖉𝖊 𝕵𝖔𝖌𝖔𝖘
    ''')
def exibir_opcoes():
    print('1. Cadastrar jogo')
    print('2. Listar jogos')
    print('3. Alterar estado do jogo')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '-' * (len(texto))
    print(linha)
    print(texto)

    print(linha)
    print()


def finalizar_app():
    os.system('cls')
    print('''Encerrando Programa 🎀''')

def opcao_invalida():
    exibir_subtitulo('Opção Inválida\n')
    input('''Digite uma tecla para reiniciar ❣ ''')
    main()

def cadastrar_novo_jogo():
    os.system('cls')
    exibir_subtitulo('Cadastrar novo jogo\n')
    nome_jogo = input('''Digite o nome do jogo ❣ ''')
    categoria = input('''Digite a categoria do jogo ❣ ''')
    dados_do_jogo = {'nome':nome_jogo, 'categoria':categoria, 'ativo':False}
    jogos.append(dados_do_jogo)
    input('''Digite uma tecla para reiniciar ❣ ''')
    main()

def listar_jogos():
    exibir_subtitulo('Listando os Jogos')
    print(f" - {'Nome do Jogo'.ljust(15)} | {'Categoria'.ljust(15)} | Status")
    for jogo in jogos:
        nome_do_jogo = jogo['nome']
        categoria_do_jogo = jogo['categoria']
        ativo_jogo = jogo['Ativo']
        print(f' - {nome_do_jogo.ljust(15)} | {categoria_do_jogo.ljust(15)} | {ativo_jogo}')

    input('''Digite uma tecla para reiniciar ❣ ''')
    main()
   
def alternar_estado_jogo():
    exibir_subtitulo('Modificar estado do jogo')
    nome_jogo = input('Digite o nome do jogo')
    for jogo in jogos:
        if nome_jogo == jogo['nome']:
            jogo['ativo'] = not jogo['ativo']

            mensagem = f'O jogo {nome_jogo} está ativado' if jogo ['ativo'] else f'O jogo {nome_jogo} está desativado' 
            print(mensagem)
            
    main()
            


def escolher_opcao():
    try:
        opcao_escolhida = int(input('''Escolha uma opção ❣ '''))
        print(f'''Você escolheu a opção 🎀 {opcao_escolhida}''')

        if opcao_escolhida == 1:
            cadastrar_novo_jogo()
        elif opcao_escolhida == 2:
            listar_jogos()
        elif opcao_escolhida == 3:
            alternar_estado_jogo()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()







