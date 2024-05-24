import pathlib  # Импорт модуля pathlib для работы с путями к файлам и директориям

import pkg_resources  # Импорт модуля pkg_resources для работы с ресурсами в пакетах Python
from setuptools import find_packages, setup  

# Функция requirements() используется для парсинга зависимостей из файлов requirements.txt и requirements-dev.txt, 
# чтобы установить их в процессе установки проекта или его дополнительных компонентов для разработки.
def requirements(filepath: str):
    # Функция requirements принимает путь к файлу с зависимостями и возвращает список зависимостей
    with pathlib.Path(filepath).open() as requirements_txt:
        return [
            str(requirement) # Преобразуем зависимости в строки
            for requirement in pkg_resources.parse_requirements(requirements_txt) # Парсим зависимости из файла
        ]


# setup.py используется для определения метаданных вашего проекта (имя, версия), 
# установки зависимостей и настройки других параметров, необходимых для правильной установки и работы вашего проекта.
setup(
    name="ml_app", # Имя вашего проекта
    version="0.1.0",
    packages=find_packages(exclude=["tests"]), # Пакеты, которые включены в ваш проект
    python_requires=">=3.9", # Версия Python, необходимая для работы вашего проекта
    install_requires=requirements("requirements.txt"), # Зависимости, необходимые для установки и работы вашего проекта
    extras_require={"dev": requirements("requirements-dev.txt")}, # Дополнительные зависимости для разработки
)
