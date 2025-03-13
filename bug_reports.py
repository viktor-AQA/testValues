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

bugs_finish = []
index_2 = 0
for new_list[index_2] in new_list:
    if 'High' in new_list[index_2]:
        bugs_finish.append(new_list[index_2])
    index_2 += 1

print(bugs_finish)

index_3 = 0
for new_list[index_3] in new_list:
    if 'Middle' in new_list[index_3]:
        bugs_finish.append(new_list[index_3])
    index_3 += 1

print(bugs_finish)
