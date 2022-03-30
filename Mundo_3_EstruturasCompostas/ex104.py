'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n')'''

def leiaInt(msg):
    while True:
        n = input('Digite um número: ')
        if n.isnumeric():
            return n
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')

#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}') 