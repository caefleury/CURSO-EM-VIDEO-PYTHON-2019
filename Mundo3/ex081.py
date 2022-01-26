lista = []
cont = 0
while True:
    lista.append(int(input("Digite um valor: ")))
    cont += 1
    answer = input("Quer continuar [S/N]: ").upper().strip()[0]
    while answer not in 'SN':
            print("Resposta inválida! Tente novamente")
            answer = input("Quer continuar [S/N]").upper().strip()[0]
    if answer == 'N':
        break
print(f"{cont} valores foram digitados.")
lista.sort(reverse=True)
print(f'Valores em ordem decrescente: {lista}')
if 5 in lista:
    print("O valor 5 FAZ parte da lista")
else:
    print("O valor 5 não faz parte da lista")