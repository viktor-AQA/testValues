print("Здорова, ты нашел баг? Составь пожалуйста баг-репорт по маске:")
print("'Название бага - приоритет (High, Middle, Low)'")

bugs = []

bugs.append(input("Заполни баг-репорт по маске: "))
bugs.append(input("Заполни баг-репорт по маске: "))
bugs.append(input("Заполни баг-репорт по маске: "))
bugs.append(input("Заполни баг-репорт по маске: "))
bugs.append(input("Заполни баг-репорт по маске: "))

new_list = []

for index, bug in enumerate(bugs):
    if 'Low' in bugs[index]:
        continue
    else: new_list.append(bugs[index])
    index += 1

print(new_list)

bugs_finish = []
for index, bug in enumerate(new_list):
    if 'High' in new_list[index]:
        bugs_finish.append(new_list[index])
    index += 1

print(bugs_finish)

index_3 = 0
for index, bug in enumerate(new_list):
    if 'Middle' in new_list[index]:
        bugs_finish.append(new_list[index])
    index += 1

print(bugs_finish)
