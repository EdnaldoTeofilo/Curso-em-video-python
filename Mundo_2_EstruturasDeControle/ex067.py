#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

print ('='*30)
print ('Tabuada de multiplicação')
print ('='*30)
while True: 
    x = int(input('Digite um número: '))
    print ('='*30)
    if x < 0:
        break
    for c in range (1,11):
        print (f'{x} x {c} = {x*c}')
    print ('='*30)
print ('Programa tabuada encerrado!')