'''
Validação de entrada para login:

João está desenvolvendo um sistema de cadastro para um site de leitura. 
Ele precisa garantir que os usuários insiram um nome de usuário e uma 
senha válidos. As regras são as seguintes:

O nome de usuário deve ter pelo menos 5 caracteres.
A senha deve ter pelo menos 8 caracteres.
João quer que o sistema continue solicitando as informações até que 
ambas as condições sejam atendidas. Quando o usuário insere dados válidos, 
o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

Crie um programa que implemente essa lógica usando um laço while.

Saída esperada:

    Digite seu nome de usuario: user
    Digite sua senha: 123
    O nome de usuario deve ter pelo menos 5 caracteres.
    Digite seu nome de usuario: user22
    Digite sua senha: 12345
    A senha deve ter pelo menos 8 caracteres.
    Digite seu nome de usuario: user22
    Digite sua senha: 123456789
    Cadastro realizado com sucesso!
'''

def validar_cadastro():
    '''Solicita nome de usuário e senha até que ambos sejam válidos.'''

    while True:
        usuario = input('Digite seu nome de usuario: ')
        senha = input('Digite sua senha: ')

        if len(usuario) < 5:
            print('O nome de usuario deve ter pelo menos 5 caracteres.')
            continue # Volta para o início do loop

        if len(senha) < 8:
            print('A senha deve ter pelo menos 8 caracteres.')
            continue # Volta para o início do loop

        # Se as duas condições forem satisfeitas:
        print('Cadastro realizado com sucesso!')
        break # Encerra o loop


# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    validar_cadastro()