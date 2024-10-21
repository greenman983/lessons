grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_1 = list(students) # переводим множество в список
students_1.sort() # сортируем по алфавиту
grades_1 = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])]
 # вычисляем средний балл по отдельным спискам

average_grades = dict(zip(students_1, grades_1)) # обьединяем списки в словарь. т.к. функция zip создает кортеж (а по факту нечитаемую фигню ))), используем функцию dict для преобразования в словарь.
print(average_grades) # средние оценки по ученикам.