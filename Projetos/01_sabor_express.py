import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}]

def exibir_nome_do_programa():
    ''' Essa função é responsável por exibir o nome estilizado do prograama na tela

    Output:
    - Exibe o nome do programa formatado em arte ASCII
    
    '''
    print("""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
    ''' Essa função exibe as opções disponíveis no menu principal
    
    Output:
    - Mostra na tela as opções numeradas para o usuário escolher
    
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Essa função é responsável por finalizar o aplicativo
    
    Output: 
    - Exibe a mensagem de finalização do aplicativo
    
    '''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    ''' Essa função retorna ao menu principal do programa
    
    Inputs:
    - Nenhum

    Output:
    - Aguarda o usuário pressionar uma tecla e chama a função main() para exibir o menu principal novamente
    
    '''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    ''' Essa função é chamada quando o usuário escolhe uma opção inválida
    
    Output:
    - Exibe uma mensagem de erro e retorna ao menu principal

    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Essa função exibe um substítulo formatado com linhas de destaque
    
    Inputs:
    - texto: string que representa o subtítulo a ser exibido

    Output:
    - Exibe o texto com linhas acima e abaixo para destaque

    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante
    
    Inputs: 
    - Nome do restaurante
    - Categoria
    
    Output:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Essa função é responsável por listar todos os restaurantes cadastrados
    
    Output:
    - Exibe na tela o nome, a categoria e o status (ativo/desativado) de cada restaurante
    
    '''
    exibir_subtitulo('Listando restaurantes')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Essa função é responsável por alternar o estado de um restaurante
    
    Inputs:
    - Nome do restaurante a ser ativado ou desativado

    Output:
    - Atualiza o estado do restaurante e exibe uma mensagem de confirmação
    
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restauramte {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal

def escolher_opcao(): 
    ''' Essa função é responsável por capturar e direcionar a escollha do usuário
    
    Inputs:
    - Número da opção escolhida pelo usuário

    Output:
    - Executa a função correspondente à opção escolhida
    
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida        

        if opcao_escolhida == 1:
              cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Essa é a função principal do programa
    
    Inputs:
    - Nenhum

    Output:
    - Limpa a tela, exibe o nome do programa, as opções e aguarda a escolha do usuário
    
    '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes() 
    escolher_opcao()

if __name__ == '__main__':
    main()