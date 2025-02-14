#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
''' Программа выводит номера автомобилей из списков доступа.
    Зелёных пускаем, красных нет!
    Списки хранятся в файлах short.db - белый и stoplist.db - чёрный списки.
    Формат записи 000:х000хх{0}н000нн
    {0} - этот сепаратор использовать для корректной подстановки '\n'
    {0} - использовать обязательно там, где больше двух запесей в строке!!!
    TODO:
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


def ochistka():
    '''чистим консоль с проверкой на Виндовс или Линукс'''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def load_data(filename):
    '''Загружает данные из файла в словарь.'''
    data = {}
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            for line in file:
                key, value = line.strip().split(':', 1)  # Разделяем по первому ':'
                data[key] = value
    except FileNotFoundError:
        print(f'Файл {filename} не найден!')
        sys.exit(1)
    except Exception as e:
        print(f'Ошибка при чтении файла {filename}: {e}')
        sys.exit(1)
    return data


def main():
    '''Основная функция программы.'''
    ochistka()

    # Загружаем данные из файлов
    d = load_data('short1.db')  # Белый список
    bad = load_data('stoplist.db')  # Чёрный список

    # Настраиваем обработчик Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # Основной цикл программы
    while True:
        print(Style.RESET_ALL + Style.BRIGHT + Fore.CYAN + "Введите номер автомобиля! 0 - для выхода")
        code = input().strip()

        if code == '0':
            break

        ochistka()

        # Проверяем номер в белом и чёрном списках
        otvet = d.get(code, f'Нет таких - {code}')
        otvet_black = bad.get(code, f'Нет таких - {code}')

        # Выводим результат
        print(Style.BRIGHT + Fore.GREEN + otvet)
        print(Fore.RED + otvet_black)


if __name__ == '__main__':
    main()
