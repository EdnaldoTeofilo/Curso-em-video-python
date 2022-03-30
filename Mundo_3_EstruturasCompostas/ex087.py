#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados. B)A soma dos valores da terceira coluna. C)O maior valor da segunda linha.
x = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
p = co = li = 0
for l in range (0,3):
    for c in range (0,3):
        x[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))

print ('-='*30)

for l in range (0,3):
    for c in range (0,3):
        if c == 2:
            co += x[l][2]
        if x[l][c] % 2 == 0:
            p += x[l][c]
        if l == 2 and x[1][c] > li:
            li = x[1][c]

        print(f'[{x[l][c]:^5}]', end ='')
    print()
   
    
print (f'A soma dos valores pares é {p}.')
print (f'A soma dos valores da terceira coluna é {co}.')   
print (f'O maior valor da segunda linha é {li}.') 