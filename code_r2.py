#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
''' Программа выводит название региона РФ по коду с номера автомобиля
вводим значение и получаем результат. 
'''
# Используем колораму для подсветки
from colorama import Fore, Back, Style

# Открываем файл на чтение
f = open('short.db', 'r', encoding='UTF-8')

d = {}
# Читаем файл в память
for line in f:
    kv = line.split(':')
    key = kv[0]
    value = kv[1]

    d[key] = value


def vvod():
    # Здесь мы работаем с юзером
    print(Style.RESET_ALL + ' Введите код региона! 0 - для выхода')
    code = input()
    if code == '0':
        exit(0)
    exist_key = code in d
    if exist_key == False:
        print(Fore.RED + 'Такого кода в базе нет!')
        vvod()

    print(Fore.GREEN + d[code])
    vvod()


vvod()
