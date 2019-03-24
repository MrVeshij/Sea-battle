import copy


X = [i for i in range(100)]



def list_ships_one():
    """Возвращает все возможные расположения для однопалубников"""
    list_1 = []
    for i in X:
        list_1.append([i])
    return list_1



def list_ships_two():
    """Возвращает все возможные расположения для двухпалубников"""
    list_2 = []
    m = None
    for i in X:
        if i != 0 and i % 10 != 0:
            list_2.append([m, i])
        if i != 0 and m + 10 < 100:
            list_2.append([m, m + 10])
        m = i
    temp = copy.deepcopy(list_2)
    for i in temp:
        i.reverse()
    list_2 += temp
    return list_2


def list_ships_third():
    """Возвращает все возможные расположения для трехпалубников"""
    list_3 = []
    k = 0
    m = None
    uncorrect_ships = [10,11,20,21,30,
                       31,40,41,50,51,
                       60,61,70,71,80,
                       81,90,91]
    for i in X:
        k += 1
        if 1 < k < 100 and k not in uncorrect_ships:
            list_3.append([m, i, k])
        if k > 1 and m + 20 < 100:
            list_3.append([m, m+10, m+20])
        m = i
    temp = copy.deepcopy(list_3)
    for i in temp:
        i.reverse()
    list_3 += temp
    return list_3


def list_ships_four():
    """Возвращает все возможные расположения для четырехпалубников"""
    list_4 = []
    k = 0
    p = None
    m = None
    uncorrect_ships = [10,11,12,20,21,22,30,
                       31,32,40,41,42,50,51,
                       52,60,61,62,70,71,72,
                       80,81,82,90,91,92]
    for i in X:
        k += 1
        if 2 < k < 100 and k not in uncorrect_ships:
            list_4.append([p, m, i, k])
        if (p or p == 0) and p + 30 < 100:
            list_4.append([p, p+10, p+20, p+30])
        m = i
        if m: p = m - 1
    temp = copy.deepcopy(list_4)
    for i in temp:
        i.reverse()
    list_4 += temp
    return list_4


def list_ships_five():
    """Возвращает все возможные расположения для пятибалубников"""
    list_5 = []
    k = 0
    p = None
    m = None
    t = None
    uncorrect_ships = [10,11,12,13,20,21,22,
                       23,30,31,32,33,40,41,
                       42,43,50,51,52,53,60,
                       61,62,63,70,71,72,73,
                       80,81,82,83,90,91,92,93]
    for i in X:
        k += 1
        if 3 < k < 100 and k not in uncorrect_ships:
            list_5.append([t, p, m, i, k])
        if (t or t == 0) and t + 40 < 100:
            list_5.append([t, t+10, t+20, t+30, t+40])
        m = i
        if m: p = m - 1
        if p: t = p - 1
    temp = copy.deepcopy(list_5)
    for i in temp:
        i.reverse()
    list_5 += temp
    return list_5