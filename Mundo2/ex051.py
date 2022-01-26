print('=' * 27)
print("     TERMOS DE UMA P.A")
print('=' * 27)

n = (int(input("Digite o primeiro termo: ")))
r = (int(input("Digita a razão: ")))

for c in range(0,10):
    print(n,' > ', end=' ')
    n += r
print("ACABOU")
