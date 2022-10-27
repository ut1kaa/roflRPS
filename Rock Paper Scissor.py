import os
import random
from time import sleep



def rps(confim):
    
    if confim == 'y':
        print('\nКрасава, начинаем играть.')
        sleep(2)
        x = game()
        if x == 1:
            sleep(2)
            print('\nКак ты меня победил еблан')
        elif x == 2:
            sleep(2)
            print('\nАхахапхахпаххп я тебе весь рот обкончал даун, ты проиграл')
        elif x == 3:
            sleep(2)
            print('\nСовпадение года ебать, ничья получается')
        elif x == 4:
            sleep(2)
            print('\nПросто боже чел иди нахуй')
    elif confim == 'n':
        print('\nНу и иди тогда в пизду')
    else:
        rps(input('\nТы еблан тебя попросили ввести <<y>> или <<n>>, введи еще раз ...\n'))
    
def game():
    rps = ['K', 'N', 'B']
    user = input('\nВведи <<K>> - камень, <<N>>- ножницы, <<B>> - бумага (АНГЛ БОЛЬШИЕ)\n')
    if user == 'K' or user == 'N' or user == 'B':
        pc = random.choice(rps)
        if user == pc:
            print(f'\nТы выбрал {user} как и я, НИХУЯ СЕБЕ ВОТ ЭТО СОВПАДЕНИЕ, иди нахуй ванга ')
            return 3
        elif user == "K":
            if pc == "N":
                print(f"\nТы выбрал {user}, а я выбрал {pc}, ты чёрт блять, как ты победил блять")
                return 1
            else:
                print(f"\nТы выбрал {user}, а я выбрал {pc}, ААХАХАХА ЕБАТЬ ТЫ БЕЗДАРЬ, ИЗИ")
                return 2
        elif user == "B":
            if pc == "K":
                print(f"\nТы выбрал {user}, а я выбрал {pc}, ты еблан блять нахуй ты так делаешь")
                return 1
            else:
                print(f"\nТы выбрал {user}, а я выбрал {pc}, ПАХПАХПХАХ БОЖЕ ЧЕЛ ТЫ ТАКОЙ НУБ")
                return 2
        elif user == "N":
            if pc == "B":
                print(f"\nТы выбрал {user}, а я выбрал {pc}, твоя мать в канаве как и ты блять, нахуй ты побеждаешь?")
                return 1
            else:
                print(f"\nТы выбрал {user}, а я выбрал {pc}, обосрал я тебя еблан")
                return 2
    else:
        print('\nИди нахуй бездарь')
        return 4

        


print('\nПривет')
sleep(2)
print('\nСейчас мы будем играть в камень, ножницы, бумага')
sleep(2)

rps(input('\nГотов? y/n\n'))