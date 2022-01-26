count = soma = media = maior = menor = 0
perg = 's'

while perg in 'Ss':
    n = int(input('Digite um número:'))
    count += 1
    soma += n
    if count == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    perg = input("Quer continuar? Digite 'S' para continuar: ").upper().strip()

if perg in 'Nn':
    media = soma / count
    print('Você digitou {} números e a media foi {:.2f}'.format(count, media))
    print(f"O maior termo foi {maior} e o menor foi {menor}")
else:
    print('Resposta invalida')



