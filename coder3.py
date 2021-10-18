#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
''' Программа выводит название региона РФ по коду с номера автомобиля
вводим значение и получаем результат. 
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
    
# Очищаем консоль перед работой
os.system('clear')

# Открываем файл на чтение
#f = open('short.db', 'r', encoding='UTF-8')
d = {}
print(type(d))
with open('short.db', 'r', encoding='UTF-8') as f:
    ''' Здесь безопасно открываем файл и сразу парсим его в словарь -d-.
    
'''
    for line in f:
        kv = line.split(':')
        #d[kv0] = kv1
        #key = kv[0]
        #value = kv[1]
        #d[key] = value


def vvod():
    # Здесь мы работаем с юзером
    
    print(Style.RESET_ALL + Fore.CYAN + "Введите код региона! 0 - для выхода")
    code = input()
    if code == '0':
        f.close()
        sys.exit(0)
    exist_key = code in d
    if exist_key == False:
        print(Fore.RED + Style.BRIGHT + 'Такого кода в базе нет!')
        #os.system('clear')
        vvod()

    print(Fore.GREEN + Back.WHITE + d[code] + Style.RESET_ALL)
    print(Style.RESET_ALL)
    vvod()

signal.signal(signal.SIGINT, signal_handler)
vvod()
signal.pause()

main()
