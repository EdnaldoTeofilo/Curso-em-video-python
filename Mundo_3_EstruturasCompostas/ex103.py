'''Faça um programa que tenha uma função chama ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''
def ficha(nome_jogador = '<desconhecido>', gols_jogador = 0):
    print(f'O jogador {nome_jogador} fez {gols_jogador} gol(s) no campeonato.')

#Programa principal

nome_jogador = str(input('Nome do jogador: ')).strip()
gols_jogador = str(input('Número de Gols: '))
if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0
if nome_jogador == '':
    ficha(gols_jogador=gols_jogador)
else:
    ficha(nome_jogador, gols_jogador)
 