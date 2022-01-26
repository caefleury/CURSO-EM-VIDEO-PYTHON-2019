from time import sleep
total = over = menor = cont = 0
print('=-' * 18)
print('       MERCADINHO BIGBOM')
print('=-' * 18)
while True:
    name = str(input('Qual o nome do produto: '))
    cont += 1
    # ------------------------------------------------ #
    price = float(input("Preço: "))
    if cont == 1:
        menor = price
        barato = name
    while price < 0:
        print("Não são permitidos números negativos!")
        price = float(input("Preço: "))
    total += price
    if price > 1000:
        over += 1
    if price < menor:
        menor = price
        barato = name

    # ------------------------------------------------------------------ #
    answer = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while answer not in 'SN':
        print("Resposta inválida!")
        answer = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

    if answer == 'N':
        break

# ------------------------------------------ #
print(" ")
print("{:-^40}".format(' FIM DO PROGRAMA '))
sleep(1)
print('PROCESSANDO ' , end='')
sleep(1)
print(".", end='')
sleep(1)
print(".", end='')
sleep(1)
print(".")
sleep(1)
print(f"O total gasto na compra foi R${total:.2f}")
print(f'{over} produtos custam mais de R$1000.00')
print('{} é o produto mais barato'.format(barato.upper()))