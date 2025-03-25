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
full_kilograms = transformation
print("В", grams, "граммах", full_kilograms, "килограмма")

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
elif is_even:
    print("Число", number_1, "не подходит под условия")
else:
    print("Число", number_1, "является отрицательным и четным")

# Задача 4

print("-------------------------------")
print("Task 4")
number_3 = 10
check_range = 0 < number_3 < 100
if check_range:
    print("Число", number_3, "находится в диапазоне от 0 до 100")
else:
    print("Число", number_3, "выходит за диапазон от 0 до 100")

# Задача 5

print("-------------------------------")
print("Task 5")
number_4 = 15
is_even_three = (number_4 % 3 == 0)
if is_even_three:
    print("Число", number_4, "кратно 3")
if not is_even_three:
    print("Число", number_4, "не кратно 3")

# Задача 1 добавление эл в список

print("-------------------------------")
print("Task 1")
numbers = [1, 2, 3, 5, 6, 7]
numbers.append(4)
print(numbers)

# Задача 2 удаление эл в список

print("-------------------------------")
print("Task 2")
numbers.remove(2)
print(numbers)

# Задача 3 получение по индексу

print("-------------------------------")
print("Task 3")
cities = ["Москва", "Париж", "Токио", "Нью-Йорк", "Берлин"]
print(cities[3])

# Задача 4 доступ по срезу

print("-------------------------------")
print("Task 4")
print(numbers[2:5])

# Задача 5 изменение элемента из списка

print("-------------------------------")
print("Task 5")
cities[3] = "Рязань"
print(cities)

# Задача 6 длина списка

print("-------------------------------")
print("Task 6")
print(len(cities))

# Задача 7 добавить элемент в словарь

print("-------------------------------")
print("Task 7")
student = {"name":"Anton", "age": 100, "universiti":"ПРТГТУ"}
student["universiti"] = "ПРТГТУ"
print(student)

# Задача 8 добавить элемент в словарь

print("-------------------------------")
print("Task 8")
student = {"name":"Anton", "age": 100, "universiti":"ПРТГТУ"}
student["universiti"] = "РГРТУ"
print(student)

# Задача 9 добавить элемент в словарь

print("-------------------------------")
print("Task 9")
student = {"name":"Anton", "age": 100, "universiti":"ПРТГТУ"}
del student["age"]
print(student)

# Задача 10 добавить элемент в словарь

print("-------------------------------")
print("Task 10")
print("Имя студента", student["name"])

# Задача 11 проверка наличия ключа

print("-------------------------------")
print("Task 11")
student = {"name":"Anton", "age": 100, "universiti":"ПРТГТУ"}
if "age" in student:
    print("ключ 'age' найден в словаре")
else:
    print("ключ 'age' не найден в словаре")

# Задача 12 изменение элемента во вложенном словаре

print("-------------------------------")
print("Task 12")
student = {
    "name":"Anton",
    "age": 100,
    "universiti":"ПРТГТУ",
    "city":{
        "address":"gup",
        "street":"Baker Street"
}
}
student["city"]["addres"] = "help"
print(student["city"]["addres"])

# Задача 13 изменение элемента в списке, находящимся в словаре

print("-------------------------------")
print("Task 13")
women = {"name":"other", "age": 24, "params":[90, 60, 90]}
women["params"][1] = 90
print(women["params"])

# Задача 14 изменение элемента в словаре, находящимся в списке

print("-------------------------------")
print("Task 14")
womens = [{"name":"other", "age": 24, "params":[90, 60, 90]}, {"name":"Katya", "age": 42, "params":[70, 60, 90]}]
womens[1]["age"] = 36
print(womens)

# Задача 15 изменение элемента в словаре, находящимся в списке

print("-------------------------------")
print("Task 15")
color = ("green", "red", "orange")
check = "green" in color
print("в кортеже есть елемент 'green' - ", check, ", а длина кортежа", len(color))