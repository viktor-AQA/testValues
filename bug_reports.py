from operator import index

print("Здорова, ты нашел баг? Составь пожалуйста баг-репорт по маске:")
print("'Название бага - приоритет (High, Middle, Low)'")

bugs = []

bugs.append(input("Заполни отчет по маске: "))
bugs.append(input("Заполни отчет по маске: "))
bugs.append(input("Заполни отчет по маске: "))
bugs.append(input("Заполни отчет по маске: "))
bugs.append(input("Заполни отчет по маске: "))
#
# for Low in bugs:
#     bugs.remove()
#
# print(bugs)
new_list = []
index = 0
for bugs[index] in bugs:
    if 'Low' in bugs[index]:
        continue
    else: new_list.append(bugs[index])
    index += 1

print(new_list)


