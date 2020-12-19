import random
from chitcube import chitcube
from cube import dice

cube1 = chitcube()
cube2 = chitcube()
cube1.value = 6

cash = 10
print('Добро пожаловать!')
while cash > 0:
    print('Баланс: ' + str(cash))
    print('Сделайте Вашу ставку:')
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
    cash = round(cash - stavka, 2)
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

    Y1 = cube1.roll()
    Y2 = cube2.roll()
    Y = Y1 + Y2

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