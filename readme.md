### Запуск приложения

    git clone https://github.com/gmoroz/test_task_stripe
    cd test_task_stripe
    docker-compose up -d

Главная страница будет доступна по адресу `http://localhost/`

### Остановка приложения:

Если надо удалить данные бд, добавьте в конце команды флаг `-v`

    docker-compose down
