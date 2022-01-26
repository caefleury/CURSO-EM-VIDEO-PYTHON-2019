#acumulador
soma = 0
#contador
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos os {} valores solicidos é {}'.format(cont,soma))

