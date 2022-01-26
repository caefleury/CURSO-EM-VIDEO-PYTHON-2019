homens = m_20 = over = 0
while True:
    print('=-' * 18)
    print('       CADASTRE UMA PESSOA')
    print('=-' * 18)
    # ------------------------------------------------- #
    # ------------------- SEXO ------------------------ #
    sexo = input("Informe o sexo [M/F]: ").upper().strip()[0]
    while sexo not in 'MF':
        sexo = input("Informe o sexo [M/F]: ").upper().strip()[0]

    # ------------------------------------------------- #
    # ------------------ IDADE ------------------------ #
    idade = int(input("Informe a idade: "))
    while idade <= 0:
        print("Idade inválida")
        idade = int(input("Informe a idade: "))

    # ------------------------------------------------- #
    # ------------ INFORMATION GATHERING -------------- #
    if idade >= 18:
        over += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            m_20 += 1
        else:
            m_20 += 0

    # ------------------------------------------------- #
    # -------------- CONTINUE OR NOT ------------------ #
    resp = input("Quer continuar? [S/N] ").upper().strip()[0]
    while resp not in 'SN':
        resp = input("Quer continuar? [S/N] ").upper().strip()[0]
    # ------------------------------------------------- #

    if resp == 'N':
            break
# ------------------ CONCLUSION ------------------ #
print(f'a) {over} pessoas tem mais de 18 anos')
print(f'b) {homens} pessoas são do gênero MASCULINO')
print(f'c) {m_20} mulheres tem menos de 20 anos')
