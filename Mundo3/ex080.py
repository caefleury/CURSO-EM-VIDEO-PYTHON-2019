list = []
for c in range(0,5):
    if c == 0:
        n = int(input(f"Digite o 1º valor: "))
        list.append(n)
        print("Valor adicionado ao começo da lista...")
    else:
        n = int(input(f"Digite o {c + 1}º valor: "))
        if n > list[-1]:
            list.append(n)
            print("Valor adicionado ao final da lista...")
        elif n < list[0]:
            print('Valor adicionado ao começo da lista..')
            list.insert(0,n)
        else:
            pos = 0
            while pos < len(list):
                if n <= list[pos]:
                    list.insert(pos, n)
                    print(f'Valor adicionado na posição {pos + 1} da lista')
                    break
                pos += 1

print(list)