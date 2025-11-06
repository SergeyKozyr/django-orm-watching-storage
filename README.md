## Пульт охраны банка
Веб приложение для мониторинга визитов в банк.

## Локальный запуск
- Создать и активировать виртуальное окружение
```shell
python -m venv venv
source venv/bin/activate
```
- Установить зависимости
```shell
pip install -r requirements.txt
```
- Настроить переменные окружения
```shell
DEBUG=<режим отладки true/false>
DB_NAME=<название бд>
DB_PORT=<порт бд>
DB_HOST=<адрес бд>
DB_USER=<пользователь бд>
DB_PASSWORD=<пароль бд>
SECRET_KEY=<секретный ключ для django>
```
- Запустить сайт
```shell
python manage.py runserver
```
- Перейти на http://0.0.0.0:8000/

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).