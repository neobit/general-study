# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da CORINTHIANS.

times = 'Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico PR', 'Atlético MG', 'Fortaleza', 'São Paulo', 'América MG', 'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino', 'Coritiba', 'Cuiabá MT', 'Ceará', 'Atlético GO', 'Avaí', 'Juventude'

print('\n\n\nOs 5 primeiros colocados do Brasileirão são: {}'.format(times[0:5]))

print('\nOs 4 ultimos colocados do Brasileirão são: {}'.format(times[-4:]))

print(f'\n\nLista de times em ordem alfabética: {sorted(times)}')

print('\nO time Corinthians está na {}ª posição.'.format(times.index('Corinthians')+1))

