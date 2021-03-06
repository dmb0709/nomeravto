#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
''' Программа выводит номера автомобилей из списков доступа. Зелёных пускаем, красных нет!
Списки хранятся в файлах short.db - белый и stoplist.db - чёрный списки.
Формат записи 000:х000хх н000нн
'''
# Используем колораму для подсветки
from colorama import Fore, Back, Style
import signal
import sys
import os


def signal_handler(sig, frame):
    ''' Эта хрень перехватывает нажатие Ctrl+C. Как работае я хз, но исправно выполняет свою функцию.  '''
    print(' Выход по Ctrl+C!')
    sys.exit(0)
    
    
# Открываем файл на чтение
f = open('short1.db', 'r', encoding='UTF-8')
f1 = open('stoplist.db', 'r', encoding='UTF-8')

# Очищаем консоль перед работой
os.system('clear')

d = {}
bad = {}

# Читаем в память файл с допуском
for line in f:
    kv = line.split(':')
    key = kv[0]
    value = kv[1]
    d[key] = value

# Читаем в память файл с "чёрным" списком
for line in f1:
    kv = line.split(':')
    key = kv[0]
    value = kv[1]
    bad[key] = value

def vvod():
    # Здесь мы работаем с юзером    
    print(Style.RESET_ALL + Style.BRIGHT + Fore.CYAN + "Введите номер автомобиля! 0 - для выхода")
    code = input()
    if code == '0':
        sys.exit(0)

    os.system('clear')
    print(Style.BRIGHT + Fore.GREEN + d.get(code, 'Нет таких') + '\n' + Fore.RED + bad.get(code, 'Нет таких'))
    vvod()

signal.signal(signal.SIGINT, signal_handler)
f.close()
vvod()
signal.pause()
