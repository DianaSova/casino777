# Casino777 предлагает Вам окунуться в мир азарта и кутежа.

import random
from cube import dice
from chitcube import chitcube

#------------------------------------------------------------
# Если Вы читер, замените dice ниже на chitcube.
#------------------------------------------------------------

cube1 = dice()
cube2 = dice()

# Если Вы играете честно, нужно закомментить следующую строку.
cube1.value = 6

# Стартовый баланс игрока
cash = 10
print('Добро пожаловать!')

# "Пока есть деньги"
while cash > 0:
    print('Баланс: ' + str(cash))
    print('Сделайте Вашу ставку:')

    # Проверка корректности ставки
    while True:
        try:
            stavka = float(input())
            if stavka > 0 and stavka <= cash:
                break
            if stavka < 0:
                print('Негативные ставки не принимаются')
            if stavka > cash:
                print('Кого ты пытаешься обмануть?')
        except:
            pass

    # Округление до двух знаков после запятой
    cash = round(cash - stavka, 2)

    # Выбор числа
    while True:
        print ('Введите число от 2 до 12:')
        try:
            X = int(input())
            if X >= 2 and X <= 12:
                break
            else:
                print('Сказал же: число от 2 до 12')
        except:
            pass

    # Кубики (кидаються)
    Y1 = cube1.roll()
    Y2 = cube2.roll()
    Y = Y1 + Y2

    # Исходя из вероятности выпадения числел и их суммы на двух кубах:    #
    if Y == X:
        if X == 7:
            stavka = stavka * 2
        if X == 6 or X == 8:
            stavka = stavka * 3
        if X == 5 or X == 9:
            stavka = stavka * 5
        if X == 4 or X == 10:
            stavka = stavka * 11
        if X == 3 or X == 11:
            stavka = stavka * 17
        if X == 2 or X == 12:
            stavka = stavka * 35
        stavka = round(stavka, 2)
        print ('Поздраляю! Ваш выигрыш ' + str(stavka))
    elif X == Y + 1 or X == Y -1:
        stavka = round(stavka + 0.1, 2)
        print('Почти угадал... Выигрыш: ' + str(stavka))
        print('Выпавшее число: ' + str(Y))
    else:
        print ('Проигрыш.')
        print ('Выпавшее число: ' + str(Y))
        stavka = 0
    cash = round(cash + stavka, 2)
print ('Приходи еще. Когда будут деньги...')