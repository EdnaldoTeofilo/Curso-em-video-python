#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final, mostre: A)Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

x =(int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')))

print(f'Você digitou os valores {x}')
print(f'O valor 9 apareceu {x.count(9)} vezes')
if 3 in x:
    print(f'A posição do primeiro valor 3: {x.index(3)}ª')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os números pares: ', end='')
for n in x:
    if n % 2 ==0:
        print(n, end=' ')