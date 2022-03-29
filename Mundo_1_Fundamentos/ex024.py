#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
x = str(input('Digite o nome da cidade: ')).strip()
print (x[:5].upper() == 'SANTO')
