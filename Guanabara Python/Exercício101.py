#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa; 
#Retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL OU OBRIGATÓRIO nas eleições 

def voto(ano):
    from datetime import date
    atual = date.today().year
    i = atual - ano
    if i < 16:
        return f'Com {i} anos: NÃO VOTA.'
    elif 16 <= i < 18 or i > 65:
        return f'Com {i} anos: VOTO OPCIONAL.'
    else:
        return f'Com {i} anos: VOTO OBRIGATÓRIO.'

#Programa principal
print('-'*30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))