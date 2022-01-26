soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {} numero: '.format(c)))
    cont += 1
    if n % 2 == 0:
        soma = soma + n
print('Você informou {} numeros e a soma dos numeros pares foi {}'.format(cont,soma))