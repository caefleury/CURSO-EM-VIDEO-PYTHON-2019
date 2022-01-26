lista = []
maior = 0
menor = 0
for c in range(1,6):
    lista.append(int(input(f"Digite o {c}° valor: ")))
    if c == 1:
        maior = menor = lista[c - 1]
    else:
        if lista[c - 1] > maior:
            maior = lista[c - 1]
        if lista[c - 1] < maior:
            menor = lista[c - 1]

print(f'Você digiou os valores: {lista}')

print(f"O maior valor é o {maior} na posição ", end='')
for pos,valor in enumerate(lista):
    if valor == maior:
        print(f'{pos + 1}...', end = '')

print(f"\nO menor valor é o {menor} na posição ", end='')
for pos,valor in enumerate(lista):
    if valor == menor:
        print(f'{pos + 1}...', end = '')
