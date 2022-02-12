#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
''' Программа выводит номера автомобилей из списков доступа.
    Зелёных пускаем, красных нет!
    Списки хранятся в файлах short.db - белый и stoplist.db - чёрный списки.
    Формат записи 000:х000хх{0}н000нн
    {0} - этот сепаратор использовать для корректной подстановки '\n'
    0 - использовать обязательно там, где больше двух запесей в строке!!!
    TODO: Нужно решить вопрос с окончанием строк в виндовых файлах!
'''
from colorama import Fore, Back, Style  # Используем колораму для подсветки
import signal
import sys
import os


def signal_handler(sig, frame):
    ''' Эта хрень перехватывает нажатие Ctrl+C.
        Как работае я хз, но исправно выполняет свою функцию.'''
    print(' Выход по Ctrl+C!')
    sys.exit(0)


# Открываем файл на чтение
f = open('short1.db', 'r', encoding='UTF-8')
f1 = open('stoplist.db', 'r', encoding='UTF-8')


def ochistka():
    '''чистим консоль с проверкой на Виндовс или Линукс'''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


d = {}
bad = {}
ochistka()
# Читаем в память файл с допуском
for stroka_fayla in f:
    razbitaya_stroka = stroka_fayla.split(':')
    # key = razbitaya_stroka[0]
    # value = razbitaya_stroka[1]
    # d[key] = value
    # Перевёл три строки в 1, читаемость так себе, но питонВей жеж!
    d[razbitaya_stroka[0]] = razbitaya_stroka[1]


# Читаем в память файл с "чёрным" списком
for stroka_fayla in f1:
    razbitaya_stroka = stroka_fayla.split(':')
    bad[razbitaya_stroka[0]] = razbitaya_stroka[1]


def vvod():
    '''Циклично получаем от пользователя номер значения и
    проверяем на присутствие в словаре такого ключа.
    Если данные присутствуют в списках - выводим в консоль'''
    # Здесь мы работаем с юзером
    text_to_user = "Введите номер автомобиля! 0 - для выхода"
    print(Style.RESET_ALL + Style.BRIGHT + Fore.CYAN + text_to_user)
    code = input()
    code = code.strip()
    if code == '0':
        sys.exit(0)

    ochistka()
    otvet = d.get(code, f'Нет таких - {code}')
    otvet_black = bad.get(code, f'Нет таких - {code}')
    print(Style.BRIGHT + Fore.GREEN + otvet.format('\n') + '\n'
          + Fore.RED + otvet_black)
    vvod()


signal.signal(signal.SIGINT, signal_handler)
f.close()
f1.close()
vvod()
signal.pause()
