import random, math, time
print("Начинаем игру в магическую консоль!")
time.sleep(1)
### Начинаем с выбора факультета. 
print("Надень шляпу, о Юный Маг!")
time.sleep(2)
print("Начинаю рАсПрЕдЕлЕнИе")
time.sleep(7)
facultet_rng = random.randint (1,4)
if facultet_rng == 1:
    print("И вы попадаете к....")
    time.sleep(3)
    print("Факультет Гриффендор!")

elif facultet_rng == 2:
    print("И вы попадаете к....")
    time.sleep(3)
    print("Факультет Слизерин")
elif facultet_rng == 3:
    print("И вы попадаете к....")
    time.sleep(3)
    print("Факультет Когтеврана")
elif facultet_rng == 4:
    print("И вы попадаете к....")
    time.sleep(3)
    print("Факультет Пуфендуй")
global event
global grifendor
global slizerin 
global kogtevran 
global puffendui 
global score
score = 0
event = random.randint(1,3)

while True:
    print("Выбери своё испытание, Юный Волшебник!")
    test = int(input())
    if test == 0:
        print ("Хочешь уйти? Уверен, о Волшебник!")
        time.sleep(1)
        print("Коль действительно уйти желаешь, то подтверди своё право покинуть зал испытаний!")
        time.sleep(1)
        print ("0 - уйти. 1 - остаться")
        leave = int(input())
        if leave == 1:
            print("Правильное решение, волшебник")
        elif leave == 0:
            print("Да будет так!")
            break



    if test == 1:
        print("Выбрано первое испытание. Настала пора угадывать заклинания")
        time.sleep(2)
        spell = random.randint(1, 100)
        print("Заклинание выбрано, настало время угадывать")
        time.sleep(3)
        if facultet_rng == 1:
            print ("Желаю удачи, Гриффиндорец")
        elif facultet_rng == 2:
            print("Желаю удачи, Слизеринец")
        elif facultet_rng == 3:
            print("Да удержат тебя твои острые когти, о Когтевранец")
        elif facultet_rng == 4:
            print("Хе-хе-хе, Пуффендуй. Это типо пуфик, да?")
        time.sleep(3)
        print("Угадывай, о Волшебник")
        global guess 
        global tries 
        tries = 0
        while True:
            guess = int(input())
            tries += 1
            if guess == spell:
                time.sleep(2)
                print("Отлично, волшебник!")
                break
            elif guess > spell:
                time.sleep(2)
                print("Твоё число больше, чем загаданное заклинание, попробуй ещё раз")
            elif guess < spell:
                time.sleep(2)
                print("Твоё число оказалось меньше загаданного, Волшебник. Попробуй ещё раз")
        time.sleep(3)        
        if tries < 3:
            print("Идеальный результат")
            score += 15
        elif 3 < tries < 7:
            print ("Достойный результат")
            score += 10
        elif 7 < tries:
            print ("От тебя ожидали большего!")
            score += 5
        time.sleep(2)
        if event == 3:
            print("Вас обнаружили за нарушением правил! Потеряйте 3 очка")
            score -= 3    
    if test == 2:
        while True:
            time.sleep(2)
            print("Выбрано испытание 2. Магический калькулятор")
            time.sleep(1)
            print("Тебе, волшебник, нужно будет ввести два числа и операцию над ними. Коль операция возможна, баллы твой факультет получит")
            time.sleep(1)
            print("Введи первое число, но помни, что число твоё целым быть должно")
            a = int(input())
            print("Теперь пора настала, второе число ввести")
            b = int(input())
            print ("Настало время операцию назвать")
            operand = input()
            operand2 = operand.lower()
            if "lumos" in (operand2):
                result = a + b
                print("Результат операции =", result)
                print("Можете радоваться, волшебник. Вы принесли баллы своему факультету")
                score += 5
                break
            elif "nox" in (operand2):
                result = a - b
                print("Результат операции =", result)
                print("Можете радоваться, волшебник. Вы принесли баллы своему факультету")
                score += 5
                break
            elif "gemino" in (operand2):
                result = a * b
                print("Результат операции =", result)
                print("Можете радоваться, волшебник. Вы принесли баллы своему факультету")
                score += 5 
                break
            elif "diffindo" in (operand2):
                if b == 0:
                    print ("Ошибочны были твои мысли и с ними числа. Невозможно делить число на 0")
                    time.sleep(1)
                    break
                else:
                    result = a // b
                    print("Результат операции =", result)
                    print("Можете радоваться, волшебник. Вы принесли баллы своему факультету")
                    score += 5
                    break
            else: 
                print("Что вы пытаетесь сколдовать!? Немедленно прекратите!")
                break
        if event == 1:
            print ("Профессор снял 4 очка за шум в библиотеке")
            score -= 4            
    if test == 3:
        while True:
            time.sleep(2)
            print("Выбрано третье испытание")
            print("Проверка артефакта")
            time.sleep(2)
            print("Вам будет дан артефакт и вашей задачей будет определить его свойства")
            time.sleep(2)
            artefact = random.randint(-100, 100)
            print("Артефакт:", artefact)
            print("Введите свойства артефакта")
            print("проклят, стабилен / проклят, нестабилен / безопасен / непроклят, нестабилен")
            specs = input().lower()
            time.sleep(2)
            if (artefact % 2 == 0) and artefact > 0:
                if "проклят" in specs and "стабилен" in specs:
                    print("Вы угадали свойства артефакта! Отличная работа")
                    score += 10
                else:
                    print("Неверно! Артефакт был проклят и стабилен.")
                break


            elif (artefact % 2 == 0) and artefact <= 0:
                if "проклят" in specs and "нестабилен" in specs:
                    print("Вы угадали свойства артефакта! Отличная работа")
                    score += 10
                else:
                    print("Неверно! Артефакт был проклят и нестабилен.")
                break

            elif (artefact % 2 != 0) and artefact > 0:
                if "безопасен" in specs or ("непроклят" in specs and "стабилен" in specs):
                    print("Вы угадали свойства артефакта! Отличная работа")
                    score += 10
                else:
                    print("Неверно! Артефакт был безопасен.")
                break

            elif (artefact % 2 != 0) and artefact <= 0:
                if "непроклят" in specs and "нестабилен" in specs:
                    print("Вы угадали свойства артефакта! Отличная работа")
                    score += 10
                else:
                    print("Неверно! Артефакт был непроклят и нестабилен.")
                break
        if event == 2:
            print("Вы случайно нашли редкий и безопасный артефакт. Получите + 6 очков")
            score += 6

if facultet_rng == 1:
    facult = "Гриффендор"
    grifendor = score
    slizerin = random.randint(-5, 20)
    kogtevran = random.randint(-5, 20)
    puffendui = random.randint(-5, 20)

elif facultet_rng == 2:
    facult = ("Слизерин")
    grifendor = random.randint(-5, 20)
    slizerin = score
    kogtevran = random.randint(-5, 20)
    puffendui = random.randint(-5, 20)    
elif facultet_rng == 3:
    facult = ("Когтевран")
    grifendor = random.randint(-5, 20)
    slizerin = random.randint(-5,20)
    kogtevran = score
    puffendui = random.randint(-5, 20)    
elif facultet_rng == 4:
    facult = ("Когтевран")
    grifendor = random.randint(-5, 20)
    slizerin = random.randint(-5,20)
    kogtevran = random.randint(-5,20)
    puffendui = score

print("🏆 Итоги соревнования факультетов:")
print("Гриффендор:", grifendor)
print("Слизерин:", slizerin)
print("Когтевран:", kogtevran)
print("Пуффендуй:", puffendui)

max_score = max(grifendor, slizerin, kogtevran, puffendui)
print("\n🥇 Победитель:")
if grifendor == max_score:
    print("Гриффендор занимает 1 место!")
elif slizerin == max_score:
    print("Слизерин занимает 1 место!")
elif kogtevran == max_score:
    print("Когтевран занимает 1 место!")
elif puffendui == max_score:
    print("Пуффендуй занимает 1 место!")
