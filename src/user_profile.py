name = input("Введите ваше имя: ")
while not name:
    print("Имя не указано. Попробуйте снова!")
    name = input("Введите ваше имя: ")
else:
    print(f"Ваш имя: {name}")

profession = input("Введите вашу профессию: ")
while not profession:
    print("Профессия не указана. Попробуйте снова!")
    profession = input("Введите вашу профессию: ")
else:
    print(f"Ваша профессия: {profession}")

tool = input("Введите ваш любимый инструмент для тестирования: ")
while not tool:
    print("Инструмент не указан. Попробуйте снова!")
    tool = input("Введите ваш любимый инструмент для тестирования: ")
else:
    print(f"Ваш любимый инструмент: {tool}. Отличный выбор!")
