#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
#Depois mostre: A) Apenas os 5 primeiros colocas. B) Os últimos 4 colocados da tabela.
#C)Uma lista com os times em ordem alfabética. D) Em que posição na tabela está o time da Chapecoense.
x = ('Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Grêmio', 'Athletico Paranaense', 'Santos', 'São Paulo', 'Internacional', 'Fluminense', 'Corinthians', 'Fortaleza', 'Bahia', 'Ceará', 'Cruzeiro', 'América Mineiro', 'Atlético Goianiense', 'Chapecoense', 'Botafogo', 'Vasco da Gama', 'Red Bull Bragantino')
print ('='*30)
print(f'Lista de times do Brasileirão por colocação: {x}')
print ('='*30)
print(f'Os primeiros 5 colocados: {x[:5]}')
print ('='*30)
print(f'Os últimos 4 colocados: {x[-4:]}')
print ('='*30)
print(f'Lista com os times em ordem alfabética: {sorted(x)}')
print ('='*30)
print (f'Posição da Chapecoense: {x.index("Chapecoense")}ª')

  