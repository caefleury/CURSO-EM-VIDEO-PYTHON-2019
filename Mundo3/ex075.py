num = (int(input('Digite um número: ')), int(input('Digite outro número: ')) ,
int(input('Digite mais um número: ')) , int(input('Digite um último  número: ')))

print(f'Você digitou os valores {num}')
print(f"O valor 9 pareceu {num.count(9)} vezes")
print(f"O valor 3 apareceu  na {num.index(3) + 1}ª posição")
pares = 0
for p in num:
    if p % 2 == 0:
        pares += 1
    else:
        pares += 0
print(f'Os valores pares digitados foi {pares}')