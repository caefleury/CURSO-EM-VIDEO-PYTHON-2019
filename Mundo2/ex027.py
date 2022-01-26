print("Digite o seu nome completo:")
nome = input().strip().title()
n = nome.split()

# ------- primeiro nome ------- #
first = n[0]

# ------- último nome ------- #
len = int(len(n))
last = n[len - 1 ]

print("O seu primeiro nome é:\033[1;33m{}\033[m".format(first))
print("O seu último nome é:\033[1;35m{}\033[m".format(last))