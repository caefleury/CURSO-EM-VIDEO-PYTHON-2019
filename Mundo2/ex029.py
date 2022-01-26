print("Digite um número: ")
numero = int(input())

# dará o "remain" de (n / 2)
n = numero % 2

if n == 0:
    #se a sobra for 0
    print("O seu número é \033[34mpar\033[m ")

else:
    #se a sobra for qualquer outra coisa alem de 0
    print("O seu número é \033[31mimpar\033[m")