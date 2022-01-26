from time import sleep
print('Ordem da matriz A(mxn): ')
m = int(input("m = "))
n = int(input("n = "))

print('Ordem da matriz B(pxq): ')
p = int(input("p = "))
q = int(input("q = "))
sleep(1)


while True:
    if n != p:
        print("Incapaz de realizar multiplicação")
        print("Os valores nas posições de 'n' e 'p' precisam ser equivalentes")
        if m == p:
            print("É possivel efetuar B x A")
            sorn = input("Deseja efetuar B x A?: ").upper()[1]
            while True:
                if 'S' in sorn:
                    # change A x B to B x A
                    break
                elif 'N' in sorn:
                    # remain
                    break
                else:
                    print(" Resposta inválida")
                    sorn = input("Deseja efetuar B x A?: ").upper()[1]
        elif n == q:


