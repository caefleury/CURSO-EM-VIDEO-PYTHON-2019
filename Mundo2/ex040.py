print("---Calculador de Notas---")
primeira = float(input("Primeira Nota: "))
segunda = float(input("Segunda Nota: "))
media = (primeira + segunda) / 2

if media < 5:
    print('Tirando {} e {}, a média do aluno é {}'.format(primeira, segunda, media))
    print("O aluno está REPROVADO")

elif 5.0 <= media <= 6.9:
    print('Tirando {} e {}, a média do aluno é {}'.format(primeira,segunda,media))
    print('O aluno está de RECUPERAÇÃO')

elif media >= 7.0:
    print('Tirando {} e {}, a média do aluno é {}'.format(primeira, segunda, media))
    print('O aluno está APROVADO')

