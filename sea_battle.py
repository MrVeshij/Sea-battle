#**Технические требования:
#+ реализация игры морской бой друг против друга (играют два человека) по стандартным правилам
#https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%80%D1%81%D0%BA%D0%BE%D0%B9_%D0%B1%D0%BE%D0%B9_(%D0%B8%D0%B3%D1%80%D0%B0)
#+ Остальные материалы в pdf-файле

#**Усложненная версия игры:
#+ Реализовать возможность выбора с кем играем: человек или компьютер
#+ Реализовать для компьютера несколько стратегий игры (то есть уровней сложности)

import random
import sys


#global values
FIELD = list(range(0,100))



def info():
	"""Описание, вывод поля"""
	print('Добро пожаловать в игру Морской бой! В данной игре у вас есть 5 кораблей как и у вашего оппонента\
		на поле 10х10 клеток. Воспользуйтесь своей аритилерией для подавляющей победы!')
	print_field()


def print_field():
	"""Рисует матрицу 10х10"""
	count = 0
	for i in FIELD:
		count += 1
		if count == 9:
			count = 0
			print(i)
		else:
			print(i,end="")


def ask_ship():
	"""Запрашивает у игрока 5 числе и формирует список кораблей"""
	count = 0
	list_ship = []
	while count != 5:
		count += 1
		try:
			ship = int(input('Введите номер клетки от 0 до 100 для установки в нее боевого корабля'))
			if ship > 100 or ship < 0:
				print('Укажите верный диапазон')
				continue
			list_ship.append(ship)
		except:
			print('Укажите число')
	return list_ship


def relist(list_ship):
	"""пересобирает изначальный список добавляя в него корабли пк либо игрока"""
	list_ship.sorted()
	relist = []
	for i in FIELD:
		if i == list_ship[0]:
			relist[i] = 'O'
			del list_ship[0]
		else:
			relist.append(i)
	return relist		


def ship_pc():
	"""Создает список кораблей пк"""
	ship_pc = []
	count = 0
	for i in range(0,100):
		count += 1
		if count == 5:
			return ship_pc
		else:
			ship_pc.append(i)


def dec(function):
	"""Смещает поле на 4 таба вправо"""
	def inner():
		print('\t\t\t\t')
		function()
	return inner


def choice_boom():
	"""Выбираем место для нанесения удара артилерией"""
	try:
		strike = int(input('Введите номер клетки для нанесения удара'))
	except:
		print('Вы указали не число')
	return strike


def mutate_list():
	"""Изменяет список кораблей пк, тем самым уничтожая корабли противника"""
	for i in pc_ship:
		if pc_ship[i] == strike:
			del pc_ship[i]
			print('Попадание')
			return pc_ship
		else:
			print('Промах')


def fict_turn():
	"""Фиктивный ход пк"""
	print('Выстрел.Промах')


def victory():
	"""Возвращает True при победе, False при поражении"""
	if pc_ship == []:
		return True
	else:
		return False


def final_message(victory):
	if victory:
		print('Вы победили!')
	elif not victory:
		print('Победил компьютер')




#main
if '__main__' == __name__:
	info()
	user_ship = ask_ship()
	pc_ship = ship_pc()
	while user_ship != [] or pc_ship != []:
		field_user = relist(user_ship)
		field_pc = relist(pc_ship)
		print_field(field_user)
		print_field(field_pc)
		strike = choice_boom()
		pc_ship = mutate_list()
		fict_turn()

	final_message()
