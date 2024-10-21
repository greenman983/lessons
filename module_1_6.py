my_dict = {'Иван': 1980, 'Петр': 1981, 'Илья': 1989, 'Сергей': 1985, 'Демид': 1988 }
print ('Список: ', my_dict)
print('Год рождения: ', my_dict['Петр'])
print('Имя из списка: ', my_dict.get('Артур', 'Отсутствует'))
my_dict.update({'Вася': 1990, 'Артем': 1983})
print(my_dict)
a = my_dict.pop('Илья')
print(a)
print('Измененный список: ', my_dict)


my_set = {1, 6, 6, 5, 5, 'max', 'john', True, (1, 2, 3)}
print('множество: ', my_set)
my_set.add(22)
my_set.add(33)
print(my_set)
my_set.discard(1)
print('Измененное множество: ', my_set)
