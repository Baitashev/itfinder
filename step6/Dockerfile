# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /itfinder-main/step6

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev libjpeg-dev zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл requirements.txt в контейнер
COPY requirements.txt /itfinder-main/step6/

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r /itfinder-main/step6/requirements.txt

# Копируем все файлы проекта из текущей директории (где Dockerfile) в контейнер
COPY . /itfinder-main/step6/

# Открываем порт, который используется Django
EXPOSE 8000

# Указываем команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
