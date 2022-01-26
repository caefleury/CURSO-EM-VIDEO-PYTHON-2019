from time import sleep
print("----- Gerador de P.A -----")
print('=-=' * 9)
first = int(input('Primeiro termo: '))
razao = int(input("Razão: "))
termo = first
cont = 1
total = 0
mais = int(input('Número de termos: '))
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA ')
    sleep(1)
    mais = int(input("Quantos termos você quer mostrar a mais?"))

print('                ----- FIM ----- ').rstrip()
print("Progressão finalizada com {} termos mostrados".format(total))

