print('=-' * 18)
print("{:-^36}".format(' BANCO PNC '))
print('=-' * 18)

n = int(input("Informe o valor a ser sacado: "))
total = n
ced = 50
n_ced = 0
while True:
    if ced <= total:
        total -= ced
        n_ced += 1
    else:
        if n_ced > 0:
            print(f"Total de {n_ced} cedulas de R${ced}")
            n_ced = 0
        # ------------- #
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        # -------------- #
        if total == 0:
            break






