idade = 0
velho = 0
final = 6
total = 0
f = 0
for c in range(1,final):
    print('-----{}ª PESSOA-----'.format(c))
    nome = input('Nome: ')
    sexo = input('Sexo [ M/F ]: ').upper().strip()
    idade = int(input('Idade: '))

    if c == 1:
        if 'M' in sexo or 'MASCULINO' in sexo:
            total += idade
            h = nome
            velho = idade
        elif 'F' in sexo or 'FEMININO' in sexo:
            total += idade
            if idade < 20:
                f += 1
            elif idade >= 20:
                f += 0
    else:
        if 'M' in sexo or 'MASCULINO' in sexo:
            total += idade
            if idade >= velho:
                velho = idade
                h = nome
            else:
                f += 0

        elif 'F' in sexo or 'FEMININO' in sexo:
            total += idade
            if idade < 20:
                f += 1
            elif idade >= 20:
                f += 0


media_idade = total / (final - 1)
print('A media da idade do grupo é de {} anos'.format(media_idade))
print("O homem mais velho é o {} e ele tem {} anos".format(h,velho))
print('{} Mulheres tem menos de 20 anos'.format(f))