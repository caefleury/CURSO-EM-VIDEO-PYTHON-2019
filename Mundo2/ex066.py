n = s = c = 0
print("Digite 999 para terminar")
while True:
    n = int(input("Digite um número: "))
    if n != 999:
        s += n
        c += 1
    else:
        break
print(f'{c} números foram digitados e a soma entre eles foi {s}')