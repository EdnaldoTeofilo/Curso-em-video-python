'''pessoas = {'nome': 'Ednaldo', 'sexo': 'M', 'idade': 20}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
#del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 89.2
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(k)'''
#x = sorted(x.items(), key =itemgetter(1), reverse=True)#Ordem importando (from operator import itemgetter)
estado = {}
brasil = []
for c in range (0, 3):
    estado ['uf'] = str(input('Unidade Federativa: '))
    estado ['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')