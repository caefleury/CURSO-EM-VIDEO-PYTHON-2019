print("~~"*15)
print("    Sequencia de Fibonacci")
print("~~"*15)

n = int(input('Quantos termos você quer mostrar: '))
print("~~"*18)
a1 = 0
a2 = 1
cont = 3
if n == 0 :
    print("Número inválido")
elif n == 1:
    print("{} ".format(a1), end='')
elif n == 2:
    print("{} > {} ".format(a1, a2), end='')
else:
    print("{} > {} ".format(a1, a2), end='')
    while cont <= n:
        cont += 1
        a3 = a2 + a1
        print('> {} '.format(a3), end='')
        a1 = a2
        a2 = a3

print('> FIM',)
print("~~"*18)
