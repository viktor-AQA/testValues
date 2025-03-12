#переменные доп задание

print("Task dop")
F = 100
transformation = (F - 32) * 5 / 9
C = round(transformation, 2)
print(C)

# Задача 1

print("-------------------------------")
print("Task 1")
grams = 2343
transformation = grams // 1000
full_killograms = transformation
print('В', grams, 'граммах', full_killograms, 'килограмма')

# Задача 2

print("-------------------------------")
print("Task 2")
number = 123
print(number %10)

# Задача 3

print("-------------------------------")
print("Task 3")
number_1 = -4
is_positive = number_1 > 0
is_even = (number_1 % 2 == 0)
if is_even and is_positive:
    print("Число", number_1, "является положительным и четным")
if not is_even:
    print("Число", number_1, "не подходит под условия")
if is_even and not is_positive:
    print("Число", number_1, "является отрицательным и четным")

# Задача 4

print("-------------------------------")
print("Task 4")
number_3 = 10
check_range = 0 < number_3 < 100
if check_range:
    print("Число", number_3, "находится в диапазоне от 0 до 100")
if not check_range:
    print("Число", number_3, "выходит за диапазон от 0 до 150")

# Задача 5

print("-------------------------------")
print("Task 5")
number_4 = 15
is_even_three = (number_4 % 3 == 0)
if is_even_three:
    print("Число", number_4, "кратно 3")
if not is_even_three:
    print("Число", number_4, "не кратно 3")