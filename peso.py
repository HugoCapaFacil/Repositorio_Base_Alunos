p = []
for i in range(5):
    pe = float(input('Digite o seu peso: '))
    p.append(pe)
    p.sort()
print(f'o imenso é {p[4]} e o graveto é {p[0]}')