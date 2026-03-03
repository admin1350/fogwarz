

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
from rich.console import Console
from rich.markdown import Markdown

# Основное меню



# Тут пользователь долженн ввести число 


# программа 1 угадай заклинание
while True:
    print("=== Магический терминал Хогвартса === =")
    print("1 - Угадай заклинание")
    print("2 - Магический калькулятор")
    print("3 - Проверка артефакта")  
    print("0 - Выход из Хогвартсаа")  
    vibor=int(input("Напишите 0-3 из меню сверху: "))
    if vibor == 0:
        break
    if vibor == 1:

        rannum = random.randint(1, 100)
        console1 = Console()
        md_text1 = """
# 1️⃣ Математический калькулятор
**Логика**
- Программа загадывает число от 1 до 100 (сила заклинания)
- Пользователь пытается угадать
- Вывод подсказок:
    - Если число меньше загаданного → "Слишком слабое заклинание!"
    - Если число больше загаданного → "Слишком мощная магия!"
    - Если угадал → "Ты настоящий волшебник!"
"""
        md1 = Markdown(md_text1)
        console1.print(md1)
    
        while True:
            n = int(input("Введите число от 1 до 100: "))
            if n < rannum:
                print("Слишком слабое заклинание!")
            elif n > rannum:
                print("Слишком мощная магия!")
            elif n == rannum:
                print("Ты настоящий волшебник!")
                break

 # программа 2 Магичекий калькулятор
    if vibor == 2:
        console = Console()
        md_text = """
# 2️⃣ **Магический калькулятор**
*Логика:*
- Пользователь вводит два числа
- Выбирает заклинание (операцию):
    - Lumos (сложение)
    - Nox (вычитание)
    - Geminio (умножение)
    - Diffindo (деление)
- Выводится результат
- Проверка деления на ноль
"""
        md = Markdown(md_text)
        console.print(md)
        prnum1=int(input("Введите 1 число: "))
        prnum2=int(input("Введите 2 число: "))

        devv=input("Введите само действие: ")

        devv2=devv.lower()
        if devv2 == "lumos" or devv2 =="nox" or devv2=="geminio" or devv=="diffindo":
            if devv2 == "lumos":
                res2=prnum1+prnum2
            elif devv2 == "nox":
                res2=prnum1-prnum2
            elif devv2 == "geminio":
                res2=prnum1*prnum2
            elif devv2 == "diffindo":
                if prnum2 == 0:
                    res2=("На ноль делить нельзя!")
                else:
                    res2=prnum1/prnum2
            print('Ответ:',res2)
        else:
            print("Такого действия не существует, проверьте правильность дествия!!!!")
        

#  программа 3 3️⃣ Проверка артефакта
    if vibor == 3:
        print(200)
        console3 = Console()
        md_text3 = """
# 3️⃣ **Проверка артефакта**
*Логика проверки:*
- Чётное число → артефакт проклят
- Положительное число → магия стабильна

*Вывод:*

- "Артефакт проклят!"
- "Магия нестабильна!"
- "Артефакт безопасен." (если не проклят и стабилен)
"""
        md3 = Markdown(md_text3)
        console3.print(md3)