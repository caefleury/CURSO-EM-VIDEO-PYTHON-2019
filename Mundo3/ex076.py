p = ('Caderno', 25.60, 'Lápis', 0.50, 'Caneta', 1.50, 'Borracha', 2.40,
     'Tesoura', 3.50, 'Cola', 2.50, 'Corretivo', 4.20,
     'Apontador', 1.50, 'Bolsa', 135.90)
print('-' * 38)
print("          TABELA DE PREÇOS         ")
print('-' * 38)
for pos in range(0,len(p)):
    if pos % 2 == 0:
        print(f'{p[pos]:.<30}',end='')
    if pos % 2 == 1:
        print(f'R$ {p[pos]}')
print('-' * 38)