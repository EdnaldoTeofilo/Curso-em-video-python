#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 
x = int(input('Digite um número:'))
y = 1
z = 0
for c in range (y,x+1):
    if x%c == 0:
        z = z + 1
    
if z == 2:
    print('O número é primo!')
else:
    print('O número não é primo!')