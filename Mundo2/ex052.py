vezes = 0
n = int(input("Digite um numero: "))

for c in range(1,n + 1):
    if n % c == 0:
        vezes += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(c, '', end='')

print('\n\033[mO numero {} foi divisível {} vezes'.format(n,vezes))

if vezes == 2:
    print("E por isso ele é \033[36mPRIMO\033[m")
else:
    print("E por isso ele \033[31mNÃO\033[m é \033[36mPRIMO\033[m")