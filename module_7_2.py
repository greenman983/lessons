def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding = 'utf-8') as file:
        for num_str, string in enumerate(strings, start = 1):
            start_str = file.tell()
            file.write(string + '\n')
            strings_positions[(num_str, start_str)] = string
    return strings_positions

file_name = 'test.txt'
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for i in result.items():
  print(i)