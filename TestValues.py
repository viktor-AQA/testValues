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