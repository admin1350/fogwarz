# from rich.console import Console
# from rich.markdown import Markdown

# console = Console()
# md_text = """
# # Заголовок
# Это **жирный** текст и *курсив*.
# - Пункт 1
# - Пункт 2
# """
# md = Markdown(md_text)
# console.print(md)









#  Импорт завимимостей
import random

# Основное меню
print("=== Магический терминал Хогвартса === =")
print("1 - Угадай заклинание")
print("2 - Магический калькулятор")
print("3 - Проверка артефакта")  
print("0 - Выход из Хогвартсаа")  


# Тут пользователь долженн ввести число 
vibor=int(input("Напишите 0-3 из меню сверху: "))

# программа 1 угадай заклинание
if vibor == 1:
    print("Логика ")
    rannum = random.randint(1, 100)
    n = int(input())

    if n < rannum:
        print("Слишком слабое заклинание!")
    elif n > rannum:
        print("Слишком мощная магия!")
    elif n == rannum:
        print("Ты настоящий волшебник!")

