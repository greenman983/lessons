first = input('Веедите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second == third: # если все равны
    print(3)
elif first == second or first == third or second == third: # если равны два из трех
    print(2)
elif first != second != third: # если все не равны
    print(0)
