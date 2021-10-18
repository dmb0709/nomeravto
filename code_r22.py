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
    
    print(Style.RESET_ALL + Fore.CYAN + "Введите номер автомобиля! 0 - для выхода")
    code = input()
    if code == '0':
        sys.exit(0)
    exist_key = code in d
    exist_key_black = code in bad
    if exist_key == False and exist_key_black == False:
        print(Fore.RED + Style.BRIGHT + 'Такого кода в базе нет!')
        vvod()
                
    os.system('clear')
    #print(Fore.GREEN + d[code] + Style.RESET_ALL)
    if d[code] == None :
        print('Error_blat')
    elif bad[code] == None:
        print('Error_blat_2')
        
    #print(d[code] || bad[code])
    print(Style.RESET_ALL)
    vvod()

signal.signal(signal.SIGINT, signal_handler)
f.close()
vvod()
signal.pause()

main()