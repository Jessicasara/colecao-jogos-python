#Explicação de como funciona: O comando print aceita um ou mais argumentos separados por vírgula.
#  Ele converte cada argumento para uma string e os exibe na saída padrão, geralmente a tela do terminal.
nome ='Jéssica'
print('Oie ', nome)

#Explicação de como funciona: O input exibe o prompt fornecido como argumento para o usuário.
# O usuário digita sua entrada e pressiona Enter. O texto digitado é então retornado como uma string.
nome = input('Digite seu nome')
print(nome)

#Explicação de como funciona: O comando if testa uma condição e executa um bloco de código se a condição for verdadeira. 
# O comando else é executado se a condição do if for falsa. O comando elif é uma combinação de else e if e é usado para verificar várias condições.
idade = 20
if idade >= 18:
    print('Você é maior de idade!')
else:  
    print('Você é menor de idade!')

#Explicação de como funciona: O for itera sobre todos os itens da sequência especificada. A variável i (ou qualquer outra variável que você escolher) 
# assume o valor de cada item da sequência em cada iteração.
for aluno in alunos:
        nome_aluno = aluno['nome']

#Explicação de como funciona: O while executa o bloco de código repetidamente enquanto a condição especificada for verdadeira. 
# É importante garantir que a condição eventualmente se torne falsa para evitar loops infinitos.
while True:
        opcao = input('Você deseja cadastrar um novo aluno? ')
        if opcao == 's':
            cadastrar_aluno()
        elif opcao == 'n':
            exibir_alunos()
            break
        else:
            print('Opção inválida')

#Explicação de como funciona: As listas são criadas usando colchetes [] e os elementos são separados por vírgulas.
#  Os elementos de uma lista podem ser acessados por meio de índices, começando em 0 para o primeiro elemento.
lista = [1, 2, 3, 4, 5]
print(lista[2])

#Explicação de como funciona: Dicionários são criados usando chaves {} e consistem em pares chave-valor separados por vírgulas.
#  Os valores são acessados usando as chaves correspondentes.
pessoa ={'nome':'Jéssica' ,'idade':28 , 'cidade':'Itajubá'}
print(pessoa['cidade'])

#Explicação de como funciona: As funções são definidas usando a palavra-chave def, seguida pelo nome da função e, opcionalmente, parâmetros entre parênteses. 
# O bloco de código da função é executado quando a função é chamada, e o resultado (se houver) é retornado com a palavra-chave return.
def somar(a, b):
    return a + b

resultado = somar(39, 28)
print(resultado)




