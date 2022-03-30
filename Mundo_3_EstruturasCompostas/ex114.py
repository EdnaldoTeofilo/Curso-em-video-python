'''Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.'''
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.google.com/')
except urllib.request.URLError:
    print('O site Google não está acessível no momento.')
else:
    print('Consegui abrir o site Google com sucesso!') 