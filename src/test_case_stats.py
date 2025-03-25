print("Здорова, ты работал всю неделю. Напиши плз, сколько ТК ты выполнил за каждый день")
cases = list()
day1 = cases.append(int(input("в пн ")))
day2 = cases.append(int(input("в вт ")))
day3 = cases.append(int(input("в ср ")))
day4 = cases.append(int(input("в чт ")))
day5 = cases.append(int(input("в пт ")))
result = 0
for sum_cases in cases:
    result += sum_cases
if (result / 5) <= 10:
    print(f"Маловато, попробуй улучшить показатели, за неделю было выполнено"
          f" {result} кейсов, усредненное кол-во кейсов за день {result / 5}")
else:
    print(f"Отличная работа, за неделю было выполнено {result} кейсов,"
          f" усредненное кол-во кейсов за день {result / 5}")