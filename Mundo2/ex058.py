from random import randint
# ----- range -----
p = 1
q = 10
n = randint(p,q)
# -----------------
tentativas = 0
print("Estou pensando em um número entre 1 e 10")
print("Será que você consegue acertar?")
print(' ----- TENTE ACERTAR -----')
num = int(input("Informe um número: "))
while num != 0:
    if num != n:
        if num < p or num > q:
            print("Número invalido")
            num = int(input("Informe um número: "))
        elif num > n:
            tentativas += 1
            print("Menos... tente mais uma vez.")
            num = int(input("Informe um número: "))
        elif num < n:
            tentativas += 1
            print("Mais... tente mais uma vez.")
            num = int(input("Informe um número: "))
    else:
        print("\033[32mVOCÊ ACERTOU!\033[m")
        print("Você acertou o número em \033[33m{} tentativa(s)\033[m".format(tentativas + 1))
        break

