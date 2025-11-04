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
python main.py
```
- Перейти на http://0.0.0.0:8000/

![img](https://github-production-user-asset-6210df.s3.amazonaws.com/43924791/509567577-e497825f-f496-4a3d-b61d-4905a68b1b79.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20251104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251104T135133Z&X-Amz-Expires=300&X-Amz-Signature=aed3ad3a23f34a18372387222422b58fb827570009d6676b28f2ef1ffca19c6e&X-Amz-SignedHeaders=host)

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).