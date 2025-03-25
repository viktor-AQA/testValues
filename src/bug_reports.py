print("Здорова, ты нашел баг? Составь пожалуйста баг-репорт по маске:")
print("'Название бага - приоритет (High, Middle, Low)'")

bugs = []

bugs.append(input("Заполни баг-репорт по маске: "))
bugs.append(input("Заполни баг-репорт по маске: "))
bugs.append(input("Заполни баг-репорт по маске: "))
bugs.append(input("Заполни баг-репорт по маске: "))
bugs.append(input("Заполни баг-репорт по маске: "))

new_list = []

for bug in bugs:
    if 'High' in bug:
        new_list.append(bug)
for bug in bugs:
    if 'Middle' in bug:
        new_list.append(bug)

print(new_list)