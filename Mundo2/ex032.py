print("-=" * 20 + "-")
print("     \033[31mInforme um número de 3 digitos\033[m ")
print("-=" * 20 + "-")
n = input()
#----------------------------------------------------------------------#
                           # Maior #
if len(n) == 3 and n[0] > n[1] and  n[0] > n[2]:
    Maior = n[0]


elif len(n) == 3 and n[1] > n[0] and  n[1] > n[2]:
    Maior = n[1]


elif len(n) == 3 and n[2] > n[1] and  n[2] > n[0]:
    Maior = n[2]


else:
    print("O número não possui 3 digitos")

#----------------------------------------------------------------------#
                           # Menor #
if len(n) == 3 and n[0] < n[1] and n[0] < n[2]:
    Menor = n[0]


if len(n) == 3 and n[1] < n[0] and n[1] < n[2]:
    Menor = n[1]


if len(n) == 3 and n[2] < n[1] and n[2] < n[0]:
    Menor = n[2]

#----------------------------------------------------------------------#
print("O menor valor é \033[36m{}\033[m e o maior valor é \033[36m{}\033[m".format(Menor,Maior))



