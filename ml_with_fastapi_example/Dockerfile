FROM python:3.10

# Копируем файлы requirements.txt, requirements-dev.txt и setup.py из текущей директории хоста в /workdir/ внутри образа
COPY requirements.txt requirements-dev.txt setup.py /workdir/
COPY app/ /workdir/app/
COPY ml/ /workdir/ml/

# Устанавливаем рабочую директорию /workdir/
WORKDIR /workdir

# Запускаем команду pip install для установки зависимостей из файла setup.py в режиме редактирования (-e)
RUN pip install -U -e .

# Запускаем приложение с помощью команды uvicorn. Здесь указывается, какое приложение и на каком хосте и порту будет запущено.
# Run the application
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]