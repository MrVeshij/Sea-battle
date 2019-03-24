# Логика - игроку в SCII графике выводится 2 поля, оба состоят из пустых клеток 10х10. Верхнее поле это поле противника
# нижнее поле это собственное поле с отображением кораблей. В начале игроку предлагается выбрать разметку для кораблей:
# 5 однопалубника, 4 двухпалубника, 3 трехпалубника, 2 четырехпалубника и 1 пятипалубник. Игрок выбирает где разместить
# корабль, путем выбора горизонтали (буквенной) и вертикали (цифренной). Корабли свыше однопалубника должны располагаться
# на одного горизонтали или вертикали при установке, крестовидные или подобные устанавливать нельзя. Также корабли
# не должны выходить за рамки поля продолжая корабль с другой стороны горизонтали/вертикали.
# В начале игры происходит рулетка в которой выбирается кто будет ходить первым, например бросок костей.
# Если ходит пк, он объявляет выстрел и рандомно выбирает клетку на поле, если пк попал но не убил корабль, он продолжает
# стрелять в соседние клетки. Если убил, объявляет победу и продолжает стрелять. Если все корабли уничтожены - игра
# заканчивается. Ход игрока - игрок выбирает клетку по горизонтали и вертикали, при промахе ход передается, при поподании,
# дается выбор повторной стрельбы. Нельзя стрелять по клеткам по которым уже стреляли.
# Корабли отрисовывать цифрами в зависимости от палуб, однопалубник это 1, пятипалубник это 5.
# На поле промах отражать крестиком X, попадания решеткой #

# Не учитывал логику когда нельзя рядом ставить корабли - доработать

# Выбор первого хода, в переменную тёрн записывается либо Н либо С
# Создаются 2 поля, одно с расстановкой кораблей пк, другое с расстановкой кораблей игрока
# В зависимости от хода, стреляет либо пк либо игрок
# Если стреляет пк, он выбирает случайное число в диапозоне 100 и если на этой клетки нет корабля, закрашивает ее знаком О
# иначе, при попадании он закрашивает место выстрела Х и стреляет повторно
# Если стреляет игрок, он выбирает место атаки, при этом после попадания отражается вражеское поле, без расставленных кораблей,
# если игрок попадает он ходит повторно, место попадения закрашивается Х иначе О
# Игра длится пока на одном из полей не останется @
# Объявляется победитель
# Доработки:
# 1) Ввести проверку на окончание игры перед вызовом функции внутри функции СДЕЛАЛ
# 2) Разделение на попал и убил, если игрок попадает в корабль, объявление "попал!" иначе "Убил!" СДЕЛАЛ
# 3) Между кораблями должен быть зазор в одну клетку, проработать логику расстановки СДЕЛАЛ
# 4) Улучшить логику хода пк при стрельбе, сейчас он стреляет рандомно в диапазоне 100, при поподании пк должен переключаться
# на новые цели которые предполагаем находятся рядом, также должна быть логика знания касаем повреждения и убийства
# 5) Улучшить визуальную часть игры, чтобы игрок видел одновременно и свою карту наравне с картой противника
# 6) Вывести код игры в продакшн, проверить на возможности оптимизации, переименовании длинных функций, рефакторинг общего кода
# 7) Проверить связки кораблей 0 10 20 30 40 50 СДЕЛАЛ


import lists_ships
import random




FIELD = [i for i in range(100)]
COUNT_SHIP = [5, 4, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1]
NAME_SHIP = ['пятипалубника', 'четырехпалубника', 'четырехпалубника',
             'трехпалубника', 'трехпалубника', 'трехпалубника',
             'двхупалубника', 'двхупалубника', 'двхупалубника',
             'двхупалубника', 'однопалубника', 'однопалубника',
             'однопалубника', 'однопалубника', 'однопалубника']
check_1 = lists_ships.list_ships_one()
check_2 = lists_ships.list_ships_two()
check_3 = lists_ships.list_ships_third()
check_4 = lists_ships.list_ships_four()
check_5 = lists_ships.list_ships_five()
CHECK_LIST = [check_1, check_2, check_3, check_4, check_5]
COMBINATIONS_SHIPS = check_3 + check_4 + check_5
CHECK_SPACE_1 = [10, 20 , 30, 40, 50, 60, 70, 80, 90]
CHECK_SPACE_2 = [9, 19, 29, 39, 49 ,59 ,69 ,79, 89]




def print_field(field):
    """Принимает на ввод список представляющий собой размещенные корабли,
    и отрисовывает поле с кораблями, пустыми поподаниями или попаданиями в корабль"""
    pr_field = field[:]
    k = 0
    for i in pr_field:
        k += 1
        if k < 10:
            print('|', i, ' |', end="")
        elif k == 10:
            print('|', i, ' |')
        elif k > 10 and k % 10 != 0:
            if i not in range(100):
                print('|', i, ' |', end="")
            else: print('|', i, '|', end="")
        else:
            if i not in range(100):
                print('|',i,' |')
            else: print('|',i,'|')



def boom_ship(field1, field2, field3, list_ships):
    """Игрок вводит число которое является его выбором для удара"""
    print_field(field2)
    while True:
        boom = input('Выберите не объявляенное для стрельбы поле:\n')
        if boom.isdigit():
            boom = int(boom)
            if boom not in range(100):
                print('Вы вышли за пределы карты.')
            elif field1[boom] != "@":
                if field1[boom] == "O" or field1[boom] == "X":
                    print('Вы уже стреляли по этому полю.')
                else:
                    print('Промах!')
                    boom = [boom]
                    update_field(field1, boom, "O")
                    update_field(field2, boom, "O")
                    print_field(field2)
                    break
            elif field1[boom] == "@":
                boom = [boom]
                print("Вы попали по вражескому кораблю!")
                update_field(field1, boom, "X")
                update_field(field2, boom, "X")
                print_field(field2) #Подсказка
                print('\n')
                if check_death(field1, list_ships, boom):
                    print('Ранен')
                else:
                    print('Убит')
                if not check_victory(field1, field3):
                    boom_ship(field1, field2, field3, list_ships)
                break
        else:
            print('Укажите номер поля.')



def boom_ship_pk(field, field2, list_ships, boom = None):
    """Возвращает поле атаки ПК"""
    """Проработка логики хода пк. Если ПК убивает корабль, то есть функция check_death дает False, то тогда
    Функция работает без изменений и задает значение boom как новое рандомное число.
    Иначе, пк атакует клетки справа или слева, если клетки вскрыты, то атака идет на вверх или вниз"""
    print('Значение boom = {}'.format(boom))
    boom = random.randrange(100)
    while True:
        if field[boom] != "@":
            if field[boom] == "X" or field[boom] == "O":
                boom = random.randrange(100)
                continue
            else:
                print('Компьютер выстрелил и промазал по полю {}'.format(boom))
                boom = [boom]
                update_field(field, boom, "O" )
                break
        else:
            boom = [boom]
            update_field(field, boom, "X")
            print('Компьютер нанес удар в поле {}'.format(boom[0]))
            if not check_victory(field, field2):
                boom_ship_pk(field, field2, list_ships, boom)
            break
            


def update_field(field, ship_list, sign):
    """Раставляет на игровое поле корабли"""
    if sign == "@" or sign == "O":
        for i in field:
            if i in ship_list:
                field[i] = sign
    else:
        temp_numb = ship_list[:]
        k = temp_numb.pop()
        field[k] = sign



def arrangement_ship(field):
    """Игрок выбирает поля на карте для размещения кораблей"""
    list_ships_player = []
    ship_temp = []
    k = 0
    print_field(field)
    for i in COUNT_SHIP:
        k += 1
        while len(ship_temp) != i:
            print('\n')
            ship = input('Введите расположение {}:\n'.format(NAME_SHIP[k-1]))
            if ship.isdigit():
                ship = int(ship)
                ship_temp.append(ship)
                if ship not in field:
                    print('Это поле уже занято')
                    ship_temp.clear()
                    continue
                elif len(ship_temp ) == i and ship_temp not in CHECK_LIST[i-1]:
                    ship_temp.clear()
                    print('Такое расположение корабля невозможно!')
                    continue
                elif check_space(field, ship_temp):
                    ship_temp.clear()
                    print('Опасность кораблекрушения! Установите корабли друг от друга не менее чем на одно поле.')
                    continue
        update_field(field,ship_temp,"@")
        list_ships_player.append(ship_temp[:])
        ship_temp.clear()
        print_field(field)
    return list_ships_player



def deploy_ships_comp(field):
    """Разворачивает корабли компъютера на игровом поле"""
    ship_temp = []
    ship_list_pk = []
    k = 0
    for i in COUNT_SHIP:
        k += 1
        random_ship = random.choice(CHECK_LIST[i-1])
        ship_temp.clear()
        while len(ship_temp) != i:
            for x in random_ship:
                if x not in field:
                    random_ship = random.choice(CHECK_LIST[i-1])[:]
                    ship_temp.clear()
                    break
                if check_space(field, random_ship):
                    random_ship = random.choice(CHECK_LIST[i-1])[:]
                    ship_temp.clear()
                    break
            else:
                ship_temp = random_ship[:]
                update_field(field, ship_temp, "@")
        ship_list_pk.append(ship_temp[:])
    return ship_list_pk



def check_space(field, ship_temp):
    """Проверяет есть ли рядом с установленным кораблем свободные клетки"""
    copy_field = field[:]
    update_field(copy_field, ship_temp, "T")
    for i in ship_temp:
        if i + 1 in range(100) and field[i + 1] == "@" and i + 1 not in CHECK_SPACE_1: return True
        elif i - 1 in range(100) and field[i - 1] == "@" and i - 1 not in CHECK_SPACE_2: return True
        elif i + 10 in range(100) and field[i + 10] == "@": return True
        elif i - 10 in range(100) and field[i - 10] == "@": return True



def check_death(field, list_ships, boom):
    """Принимает на вход список расставленных кораблей и точку в которую стреляет игрок/пк.
    Проверяет попадание, если ранение возвращает True, иначе при попадании возвращает False"""
    k = -1
    boom = boom.pop()
    for i in list_ships:
        k += 1
        for x in i:
            if x == boom:
                for c in list_ships[k]:
                    if field[c] == "@":
                        return True



def yes_no():
    """Получает yes или no от игрока"""
    while True:
        question = input('Вы хотите ходить первым?(y/n)\n').lower()
        if question == 'y' or question == 'n':
            break
    return question



def define_turn():
    """Определяет очередность ходов, возвращает токены игрока и пк"""
    question = yes_no()
    if question == 'y': return 'H'
    else: return 'C'



def check_victory(field1, field2):
    """Проверка на победителя"""
    if "@" not in field1:
        print("Победил компьютер!")
        return True
    elif "@" not in field2:
        print("Победил игрок!")
        return True



def main():
    """Запускающий модуль игры"""
    boom = None
    field_player = FIELD[:]
    field_pk = FIELD[:]
    field_pk_show = FIELD[:]
    turn = define_turn()
    #list_ships_player = arrangement_ship(field_player)
    list_ships_player = deploy_ships_comp(field_player)
    list_ships_pk = deploy_ships_comp(field_pk)
    while not check_victory(field_player, field_pk):
        if turn == "H":
            print('Ходит игрок')
            boom_ship(field_pk, field_pk_show, field_player, list_ships_pk)
            turn = "C"
        else:
            print('Ходит ии')
            boom_ship_pk(field_player, field_pk, list_ships_player, boom)
            print_field(field_player)
            turn = "H"


main()




