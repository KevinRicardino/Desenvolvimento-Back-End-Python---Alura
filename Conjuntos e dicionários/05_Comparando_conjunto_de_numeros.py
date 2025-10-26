'''
Comparando conjunto de números:

Joana é gerente de projetos e precisa consolidar as listas de 
tarefas de duas equipes distintas. Após unir as listas, ela quer 
remover uma tarefa específica informada pelo usuário. Sua tarefa 
é criar um programa que realize essa operação.

Exemplo de entrada:

    equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 
    equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"} 

Saída esperada:

    Tarefas finais: {'implementar funcionalidade', 'planejar reunião', 'revisar documento', 'corrigir bug'} 
'''

def consolidar_tarefas():
    '''Consolida as tarefas das duas equipes e remove a tarefa informada pelo usuário.'''

    # Solicita as tarefas das duas equipes
    tarefas_a = input('Digite as tarefas da equipe A (separadas por vírgula): ')
    tarefas_b = input('Digite as tarefas da equipe B (separadas por vírgula): ')

    # Converte em conjuntos, removendo espaços extras, mantendo a capitalização
    conjunto_a = {tarefa.strip() for tarefa in tarefas_a.split(',')}
    conjunto_b = {tarefa.strip() for tarefa in tarefas_b.split(',')}

    # Une os conjuntos
    tarefas = conjunto_a | conjunto_b # união dos conjuntos

    # Solicita a tarefa a ser removida
    tarefa_remover = input('Digite a tarefa a ser removida (exatamente como está): ').strip()

    if tarefa_remover in tarefas:
        tarefas.remove(tarefa_remover)

    # Exibe a saída exatamente como no exercício
    print('Tarefas finais:', tarefas)

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    consolidar_tarefas()