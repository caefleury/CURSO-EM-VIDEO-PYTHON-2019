print("\033[31m-=\033[m" * 19)
print("\033[33m==========LOJAS JUDEU SAFADO==========\033[m")
print("\033[31m-=\033[m" * 19)
cores = {'azul' : '\033[34m',
         'limpa' : '\033[m'}
price = float(input("Preço das compras: R$"))

print("""FORMAS DE PAGAMENTO:
[ 1 ] A vista {}dinheiro/cheque{}
[ 2 ] A vista no {}cartão{}
[ 3 ] Em ate {}2x no cartão{}
[ 4 ] Em {}3x ou mais{} no cartão""".format(cores['azul'],cores['limpa'],cores['azul'],cores['limpa'],cores['azul'],cores['limpa'],cores['azul'],cores['limpa']))
option = input('Informe a opção: ')

if '1' in option:
    new = price - price * 0.1
    print("Sua compra da R${} vai  custar R${} no final".format(price,new))
elif '2' in option:
    new = price - price * 0.05
    print("Sua compra da R${} vai  custar R${} no final".format(price,new))
elif '3' in option:
    print("Sua compra da R${} manterá preço no final".format(price))
elif '4' in option:
    new = price + price * 0.2
    print("Sua compra da R${} vai  custar R${} no final".format(price, new))
else:
    print("Opção invalida")
