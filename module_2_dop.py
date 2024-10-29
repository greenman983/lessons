n = int(input("Введите целое число от 3 до 20: "))
if n > 20 or n < 3:
    print('Неверное число')
else:
    slot_2 = []
    for i in range(1, 21):
        for j in range(1, 21):
            if n % (i + j) == 0 and i <= j:
                slot_2.append((i,j))
    print(*slot_2, sep=',')

