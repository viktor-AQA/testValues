'''
переменные доп задание
'''

F = 100
transformation = (F - 32) * 5 / 9
C = round(transformation, 2)
print(C)

# Задача 1

grams = 2343
transformation = grams // 1000
full_killograms = transformation
print('В', grams, 'граммах', full_killograms, 'килограмма')

# Задача 2

number = 123
print(number %10)

# Задача 3

number_1 = -4
is_positive = number_1 > 0
is_even = (number_1 % 2 == 0)
if is_even and is_positive:
    print("Число", number_1, "является положительным и четным")
if not is_even:
    print("Число", number_1, "не подходит под условия")
if is_even and not is_positive:
    print("Число", number_1, "является отрицательным и четным")