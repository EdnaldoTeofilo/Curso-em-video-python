'''x = list(range(0,10))
x[2] = 9
x[5] = 12
x.append(10)
x.sort(reverse=True)
x.insert(3, 24)
x.pop()
x.pop(7)
if 15 in x:
    x.remove(15)
else:
    print('Não achei o número 15.')
print (x)
print (f'Essa tem lista tem {len(x)} elementos.')'''

'''x = []
for cont in range(0,5):
    x.append(int(input('Digite um número: ')))

for i,v in enumerate(x):
    print(f'Na posição {i} encontrei o valor {v}')'''

a = [6, 4, 3 ,2]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')