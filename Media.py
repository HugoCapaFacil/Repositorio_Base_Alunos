n = 0
for i in range(4):
    nota = float(input('Digite a Sua nota: '))
    if nota > 0:
        n += nota/4
        if n >= 7:
            print(f'Sua nota é {n} você está aprovado')
        elif n >= 4:
            print(f'Sua nota é {n} você está em recuperação')
        elif n < 4:
            print(f'Sua nota é {n} você está reprovado')
    else:
        print('Valor invalido')