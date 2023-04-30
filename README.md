# Хаканет

### Инструкция по настройке проекта:

1. Склонировать проект
2. Открыть проект в PyCharm с наcтройками по умолчанию
3. Создать виртуальное окружение (через settings -> project "Hakanet2023" -> project interpreter)
4. Открыть терминал в PyCharm, проверить, что виртуальное окружение активировано.
5. Обновить pip:
   ```bash
   pip install --upgrade pip
   ```
6. Установить в виртуальное окружение необходимые пакеты:
   ```bash
   pip install -r requirements.txt
   ```
7. Установить в виртуальное окружение переменную для запуска:
   * Windows:
      ```bash
      $env:Server_starts="false"
      ```
   * Linux:
      ```bash
      export Server_starts="false"
      ```
8. Синхронизировать структуру базы данных с моделями:
   ```bash
   python manage.py migrate
   ```
9. Создать конфигурацию запуска в PyCharm (файл `manage.py`, опция `runserver`)

### Django Tips and Tricks

* Создать миграцию базы данных:
   ```bash
   python manage.py makemigrations
   ```
* Накатить миграции базы данных:
   ```bash
   python manage.py migrate
   ```
* Создать суперпользователя:
   ```bash
   python manage.py shell -c "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('vasya', '1@abc.net', 'promprog')"
   ```

### Docker start guid

1. Download needed image
   ```bash
   docker pull python:3.10
   ```
2. Build your image
   ```bash
   docker build . --tag main
   ```
3. Run you image
   ```bash
   docker run -p 8000:8000 -d main
   ```
4. Stop you container
   ```bash
   docker stop CONTAINER_ID
   ```
5. Start you container
   ```bash
   docker start CONTAINER_ID
   ```
6. Logs of container
   ```bash
   docker logs CONTAINER_ID
   ```

### Tips and Tricks

1. To show all images
    ```bash
       docker images
    ```
2. To show all containers
    ```bash
       docker ps
    ```
3. To show all containers (finished)
    ```bash
       docker ps -a
    ```
4. To delete image
    ```bash
       docker rmi IMAGE_ID(or image tag)
    ```
5. To delete container
    ```bash
       docker rm CONTAINER_ID
    ```
6. Log in container
    ```bash
       docker exec -it CONTAINER_ID
    ```
