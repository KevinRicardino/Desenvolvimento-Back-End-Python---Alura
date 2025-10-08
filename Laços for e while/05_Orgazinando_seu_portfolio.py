'''
Organizando seu portfólio:

Ana está desenvolvendo seu portfólio para exibir os projetos de Python que concluiu. 
Ela organizou uma lista com o nome de cada projeto, mas percebeu que alguns itens 
podem estar ausentes, aparecendo como None:

   projetos = ['website', 'jogo', 'análise de dados', None, 'aplicativo móvel']

Crie um programa que ajude Ana a percorrer a lista de projetos e exiba os nomes dos 
projetos válidos. Se encontrar um item None, o programa deve exibir a mensagem: "Projeto ausente".

Saída esperada:

   website
   jogo
   anáalise de dados
   Projeto ausente
   aplicativo móvel
'''

def exibir_projetos():
   '''Percorre a lista de projetos e exibe os válidos, indicando quando um está ausente.'''

   projetos = ['website', 'jogo', 'análise de dados', None, 'aplicativo móvel']

   for projeto in projetos:
      if projeto is None:
         print('Projeto ausente')
      else:
         print(projeto)   

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
   exibir_projetos()