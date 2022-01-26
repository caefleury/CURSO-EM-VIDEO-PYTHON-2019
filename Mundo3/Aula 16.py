lanche = ('Hamb', 'Suco', 'Pizza','Casa')
#lanche[0] = 'Hamb'

# ----- Sem posição ->
for comida in lanche:
    print(f'Eu vou comer {comida}')
print(" ")

# ----- Com posição ->
for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')

print(" ")

for pos,comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")

# ---------------------------------------------#

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(c.count(5))
# mostrará quantas vezes aparecem o número 5 em c


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.index(5))