n = 0
cont = 0
for c in range(1,11):
    n += n
    cont += 1
    print(f'{n} x {:2} = {}'.format(cont,n))
