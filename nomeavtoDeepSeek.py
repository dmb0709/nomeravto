#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
''' Программа выводит номера автомобилей из списков доступа. Зелёных пускаем, красных нет!
Списки хранятся в файлах short.db - белый и stoplist.db - чёрный списки.
Формат записи 000:х000хх н000нн
'''
import signal
import sys
import os


def signal_handler(sig, frame):
    ''' Эта хрень перехватывает нажатие Ctrl+C. Как работае я хз, но исправно выполняет свою функцию.  '''
    print(' Выход по Ctrl+C!')
    sys.exit(0)
    

# Очищаем консоль перед работой
os.system('clear')

d = {}
bad = {}

# Читаем в память файл с допуском
try:
    with open('short1.db', 'r', encoding='UTF-8') as f:
        for line in f:
            kv = line.strip().split(':')
            if len(kv) == 2:
                d[kv[0]] = kv[1]
except Exception as e:
    print("\033[31mОшибка при чтении файла short1.db:\033[0m", e)
    sys.exit(1)

# Читаем в память файл с "чёрным" списком
try:
    with open('stoplist.db', 'r', encoding='UTF-8') as f1:
        for line in f1:
            kv = line.strip().split(':')
            if len(kv) == 2:
                bad[kv[0]] = kv[1]
except Exception as e:
    print("\033[31mОшибка при чтении файла stoplist.db:\033[0m", e)
    sys.exit(1)


def vvod():
    # Здесь мы работаем с юзером    
    while True:
        print("\033[0m\033[1;36mВведите номер автомобиля! 0 - для выхода\033[0m")
        code = input()
        if code == '0':
            sys.exit(0)

        os.system('clear')
        print("\033[1;32m" + d.get(code, 'Нет таких') + "\n\033[1;31m" + bad.get(code, 'Нет таких') + "\033[0m")


signal.signal(signal.SIGINT, signal_handler)
vvod()
