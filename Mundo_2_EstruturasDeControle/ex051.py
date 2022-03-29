#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
x = int(input('Digite o primeiro número do termo:')) 
y = int(input('Digite a razão da PA:'))
print('Os 10 primeiros termos dessa progressão é:')
for c in range (0,10):
    print(x)
    x = x + y