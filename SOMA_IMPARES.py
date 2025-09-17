m = 0
for i in range(1,31,2):
    if i % 3 == 0:
        print(i, end=',')
        m += i
print(f' A soma dos numeros impares mutiplos de 3')