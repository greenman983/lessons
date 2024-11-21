def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(1, 'строка', True)
print_params(5, 'строка 2', False)
print_params(a = 1, b = 2, c = 3)
print_params(a = False, b = True, c = False)
print_params(a = 'Иван', c = 'Борис')
print_params(a = 'Sergey', b = 'line')
print_params(a = 1243124)
print_params(b = (12, 13, 14))
print_params(c = [1, 'line', True])

print(                           )

print_params()

print(                           )

print_params(b = 25)
print_params(c = [1, 2, 3])

print(                           )

values_list = ['string', 12345, True]
values_dict = {'a' : 10, 'b' : 'text', 'c' : False}

print_params(*values_list)
print_params(**values_dict)

print(                           )

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)