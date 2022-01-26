from datetime import date
ano = int(date.today().year)

pessoa = 0
maiores = 0
menores = 0
for c in range(1,8):
    pessoa += 1
    n = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    if ano - n >= 18:
        maiores +=1
    elif ano - n < 18:
        menores +=1
print("Ao todo tivemos {} pessoas maiores de idade.".format(maiores))
print("E também tivemos {} pessoas menores de idade.".format(menores))

