'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: 
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings da função.'''

def notas(*n, sit = False):
    
    """
        -> Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias).
        :param sit: valor opcional, indicando se deve ou não adicionar a situação.
        :return: dicionário com várias informações sobre a situação da turma.
    """

    resp = {}
    resp ['total'] = len(n)
    resp ['maior'] = max(n)
    resp ['menor'] = min(n)
    resp ['média'] = sum(n)/len(n)
    if sit:
        if resp ['média'] >= 7:
            resp ['situação'] = 'BOA'
        elif resp ['média'] < 5:
            resp ['situação'] = 'RUIM'
        else:
            resp ['situação'] = 'RAZOÁVEL'
    
    print ('-='*40)
    return resp

#Programa principal
resp = notas(2, 5, 10, 6.5)
help(notas)
print(resp) 