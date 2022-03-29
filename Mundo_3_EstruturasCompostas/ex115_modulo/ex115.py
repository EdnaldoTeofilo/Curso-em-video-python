"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo
seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas
as pessoas cadastradas.
"""

from ex115_modulo.lib.interface import *
from ex115_modulo.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas ', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arguivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opcão de dadastrar uma nova pessoa.
        cabeçalho ( 'NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opcão de sair do sistema.
        cabeçalho ( 'Saindo do sistema... Até logo!')
        break
    else: 
        # Digitou uma opção errada no menu.
       print('\033[31mERRO! Digite uma opcão válida!\033[m')
    sleep(2)