def metade(preço = 0, formatado = False):
    res = preço / 2
    return res if formatado is not False else moeda(res)

def dobro(preço = 0, formatado = False):
    res = preço * 2
    return res if formatado is not False else moeda(res)

def aumentar(preço = 0, taxa = 0, formatado = False):
    res = preço + (preço * taxa/100)
    return res if formatado is not False else moeda(res)

def diminuir(preço = 0, taxa = 0, formatado = False):
    res = preço - (preço * taxa/100)
    return res if formatado is not False else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(valor = 0, aumento = 10, diminui = 5):
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor)}')
    print(f'Metade do preço: \t{metade(valor)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento)}')
    print(f'{diminui}% de redução: \t{diminuir(valor, diminui)}')
    print('-' * 30)
