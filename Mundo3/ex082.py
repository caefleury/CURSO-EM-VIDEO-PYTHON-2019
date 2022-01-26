lista = []
pares = []
impares = []
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
    answer = input("Quer continuar [S/N]: ").upper().strip()[0]
    while answer not in 'SN':
        print("Resposta inválida. Tente novamente.")
        answer = input("Quer continuar [S/N]: ").upper().strip()[0]
    if answer == 'N':
        break
print(f'Lista: {lista}')
print(f'Pares: {pares}')
print(f"Ímpares: {impares}")


