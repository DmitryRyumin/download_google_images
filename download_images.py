#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Массовая загрузка изображений из txt файла
python download_images.py
    --urls путь_к_текстовому_файлу_с_URLs_изображений
    --dir_output путь_к_директории_куда_будут_сохранены_изображения
"""

# ######################################################################################################################
# Импорт необходимых инструментов
# ######################################################################################################################
import argparse  # Парсинг аргументов и параметров командной строки
import requests  # Отправка HTTP запросов
import cv2  # Алгоритмы компьютерного зрения
import os  # Работа с файловой системой

from datetime import datetime  # Работа со временем
from imutils import paths


# ######################################################################################################################
# Выполняем только в том случае, если файл запущен сам по себе
# ######################################################################################################################
def main():
    # ------------------------------------------------------------------------------------------------------------------
    # Построение аргументов командной строки
    # ------------------------------------------------------------------------------------------------------------------
    ap = argparse.ArgumentParser()  # Парсер для параметров командной строки

    ap.add_argument('--urls', required = True, help = 'Путь к текстовому файлу с URLs изображений')
    ap.add_argument('--dir_output', required = True, help = 'Путь к директории, куда будут сохранены изображения')

    args = vars(ap.parse_args())  # Преобразование списка аргументов командной строки в словарь

    # ------------------------------------------------------------------------------------------------------------------

    green = '\033[92m'  # Зеленый
    red = '\033[91m'  # Красный
    bold = '\033[1m'  # Жирный
    end = '\033[0m'  # Выход

    format_time = '%Y-%m-%d %H:%M:%S'  # Формат времени

    # ------------------------------------------------------------------------------------------------------------------

    # Файл не найден
    if os.path.isfile(args['urls']) is False:
        print('[{}{}{}] Файл "{}" не найден ...'.format(
            red, datetime.now().strftime(format_time), end, os.path.basename(args['urls'])
        ))
        return False

    _, ext = os.path.splitext(args['urls'])  # Расширение файла

    if ext.replace('.', '') != 'txt':
        print('[{}{}{}] Расширение файла должно быть "{}" ...'.format(
            red, datetime.now().strftime(format_time), end, 'txt'
        ))
        return False

    if os.stat(args['urls']).st_size == 0:
        print('[{}{}{}] Файл "{}" пуст ...'.format(
            red, datetime.now().strftime(format_time), end, os.path.basename(args['urls'])
        ))
        return False

    # Создание директории, куда будут сохранены изображения, если она не существует
    if not os.path.exists(args['dir_output']):
        os.makedirs(args['dir_output'])

    # ------------------------------------------------------------------------------------------------------------------

    # Список URL-адресов из входного текстового файла
    urls = open(args['urls']).read().strip().split('\n')

    # Проход по всем url
    for i, url in enumerate(urls):
        i += 1

        try:
            req = requests.get(url, timeout = 10)  # Отправка запроса GET

            # Сохранение изображения в указанную директорию
            path = os.path.sep.join([args['dir_output'], '{}.jpg'.format(str(i).zfill(8))])

            with open(path, 'wb') as file:
                file.write(req.content)
        except:
            print('[{}{}{}] Ошибка при загрузка "{}" ...'.format(
                red, datetime.now().strftime(format_time), end, path
            ))

    # ------------------------------------------------------------------------------------------------------------------

    all_download_files = 0  # Общее количество загруженных изображений

    # Проверка скачанных файлов
    for imagePath in paths.list_images(args['dir_output']):
        delete = False  # По умолчанию файл не должен быть удален

        try:
            image = cv2.imread(imagePath)  # Попытка чтения изображения

            # Удаление файла если он не прочитан
            if image is None:
                delete = True
            else:
                all_download_files += 1
        except:
            delete = True

        # Удаление файла
        if delete:
            print('[{}{}{}] Ошибка при чтении "{}" ... удаление ...'.format(
                red, datetime.now().strftime(format_time), end, imagePath
            ))
            os.remove(imagePath)

    print('[{}{}{}] Всего файлов загружено: {}{}{} ...'.format(
        green, datetime.now().strftime(format_time), end, bold, all_download_files, end
    ))


if __name__ == "__main__":
    main()
