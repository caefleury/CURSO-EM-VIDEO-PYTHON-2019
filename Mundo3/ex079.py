list = []
while True:
    n = int(input("Digite um valor: "))
    if n in list:
        print('Valor duplicado não vou adicionar!')
    else:
        list.append(n)
    answer = input("Quer continuar [S/N]").upper().strip()[0]
    while True:
        if answer not in 'SN':
            print("Resposta inválida! Tente novamente")
            answer = input("Quer continuar [S/N]").upper().strip()[0]
        else:
            break
    if answer == 'N':
        break
print('PROGRAMA FINALIZADO!')
list.sort()
print(list)

