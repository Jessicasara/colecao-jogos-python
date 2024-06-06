import os

def exibir_nome_do_programa():
    print('''
    𝕮𝖔𝖑𝖊𝖈̧𝖆̃𝖔 𝖉𝖊 𝕵𝖔𝖌𝖔𝖘
    ''')
def exibir_opcoes():
    print('1. Cadastrar jogo')
    print('2. Listar jogos')
    print('3. Ativar jogo')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('''𝓔𝓷𝓬𝓮𝓻𝓻𝓪𝓷𝓭𝓸 𝓹𝓻𝓸𝓰𝓻𝓪𝓶𝓪 🎀''')

def opcao_invalida():
    print('''𝓸𝓹𝓬̧𝓪̃𝓸 𝓲𝓷𝓿𝓪́𝓵𝓲𝓭𝓪\n''')
    input('''Digite uma tecla para reiniciar ❣ ''')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('''Escolha uma opção ❣ '''))
        print(f'''Você escolheu a opção 🎀 {opcao_escolhida}''')

        if opcao_escolhida == 1:
            print('''Cadastro de jogos 🎀 ''')
        elif opcao_escolhida == 2:
            print('''Listar os jogos 🎀''')
        elif opcao_escolhida == 3:
            print('''Ativar jogo 🎀''')
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







