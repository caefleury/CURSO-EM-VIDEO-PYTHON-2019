from datetime import date
print("Que ano quer analisar? Coloque 0 para analisar o atual: ")
ano = int(input())

n = date.today().year

if ano == 0:
    print("O ano {} \033[1;31mnão\033[m é bissexto".format(n))

elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é \033[1;34mBISSEXTO\033[m".format(ano))

else:
    print("O ano {} \033[1;31mnão\033[m é bissexto".format(ano))