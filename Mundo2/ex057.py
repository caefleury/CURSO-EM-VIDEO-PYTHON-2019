n = input("Digite o seu nome: ")
s = str(input("Informe o seu sexo [M/F]:")).upper().strip()

while s not in 'MF':
    print('Resposta inválida')
    s = input("Olá {} digite o seu sexo [M/F]: ".format(n))

if s == 'M':
    print('Sexo M registrado com sucesso')
    print("nome:'{}' - sexo: Masculino".format(n.title()))
elif s == 'F':
    print('Sexo F registrado com sucesso')
    print("nome:'{}' - sexo: Feminino".format(n))
