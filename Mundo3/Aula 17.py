num = [2, 3, 4, 4, 5, 7]

# Adding items
num.append(1)
num.insert(4,6)

# Sorting/Putting in order
num.sort()
num.sort(reverse=True)

# Will Remove last item:
num.pop()
del num[2]
num.remove(7)
num.remove(4) # Will take out only one number

# Removing items that can be in the list:
if 6 in num:
    num.remove(6)
else:
    print('Não achei o número 6')

#print(num)

# ----------------------------------------------------------------#
valores = []
for c in range(1,6):
    valores.append(int(input(f"Digite o {c}° valor: ")))

for pos,valor in enumerate(valores):
    print(f'Encontrei o valor {valor} na posição {pos + 1}')
print("FIM")

# ----------------------------------------------------------------#

# --------     COMO FAZER UMA COPIA DE UMA LISTA       ---------- #

# LIGAÇÃO:
a = [1, 2, 5, 7, 4]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# COPIA:
a = [1, 2, 5, 7, 4]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')