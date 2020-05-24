# Массовая загрузка изображений из Google Images

![GitHub top language](https://img.shields.io/github/languages/top/DmitryRyumin/download_google_images)
![GitHub repo size](https://img.shields.io/github/repo-size/DmitryRyumin/download_google_images)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/DmitryRyumin/download_google_images)
![GitHub last commit](https://img.shields.io/github/last-commit/DmitryRyumin/download_google_images)

#### `1` Найти необходимые изображения

> При необходимости сделать скроллинг страницы

<h4 align="center"><img src="./img/1.png" alt="1" width="70%" /></h4>

#### `2`  Открыть консоль браузера и выполнить код из [console.js](https://github.com/DmitryRyumin/download_google_images/blob/master/console.js)

> Должен быть загружен текстовый файл с URLs всех изображений

<h4 align="center"><img src="./img/2.png" alt="2" width="70%" /></h4>

#### `3` Выполнить код из [download_images.py](https://github.com/DmitryRyumin/download_google_images/blob/master/download_images.py)

##### Необходимые зависимости

| Пакеты | Текущая версия |
| ------ | -------------- |
`imutils` | ![PyPI](https://img.shields.io/pypi/v/imutils) |
`requests` | ![PyPI](https://img.shields.io/pypi/v/requests) |
`opencv-contrib-python` | ![PyPI](https://img.shields.io/pypi/v/opencv-contrib-python) |

<h4 align="center"><span style="color:#EC256F;">Пример</span></h4>

| Файлы/скрипты | Аргументы командной строки | Описания |
| ------------- | -------------------------- | -------- |
| [download_images.py](https://github.com/DmitryRyumin/download_google_images/blob/master/download_images.py) | `--urls str` - Путь к текстовому файлу с URLs изображений<br>`--dir_output str` - Путь к директории, куда будут сохранены изображения | Массовая загрузка изображений из Google Images |

<h4 align="center"><img src="./img/3.png" alt="3" width="100%" /></h4>
