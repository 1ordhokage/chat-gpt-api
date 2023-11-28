# Задача
Разработать упрощенный API-аналог ChatGPT.

Технологический стек:
- SQLAlchemy 2.0
- FastAPI
- Aiohttp
- Async
- JWT для аутентификации

Endpoints:
1. Регистрация пользователя: Пользователь должен иметь возможность регистрироваться в системе.
2. Получение данных пользователя: Реализовать возможность получения данных о зарегистрированном пользователе.
3. Отправка запроса (вопроса): Пользователь может отправить текстовый запрос (вопрос).
4. Получение сообщений: Пользователь может получить список своих последних сообщений.

Требования к реализации:
1. Функционал чатов не требуется: Сосредоточьтесь на API, игнорируя реализацию полноценного чата.
2. Формат ответа: Не важно, будет ли ответ предоставлен в режиме реального времени (stream) или нет.
3. История запросов: API должен сохранять историю последних трех запросов пользователя.
4. Обработка запросов: Не используйте библиотеку OpenAI. Работайте напрямую с запросами и ответами.
5. Авторизация: Используйте JWT для аутентификации пользователей.
6. Отслеживание пользователя: В системе должно быть понимание, какой пользователь отправил запрос или сообщение.

Ожидаемый результат:
- Код API, соответствующий вышеописанным требованиям.
- Документация к API, включая описание эндпойнтов и примеры использования.

Срок выполнения: 
Сутки с момента получения задания 
Формат сдачи:
- Исходный код на GitHub/GitLab или в виде архива.
- README файл с инструкциями по запуску и использованию API.

Оценка работы:
Ваша работа будет оцениваться по следующим критериям:
- Соответствие функциональным требованиям.
- Качество кода и его организация.
- Наличие и качество документации.
- Эффективность и оптимизация решения.


## Линтеры:

Максимальная длина строк - 88 в соответсвии с Black (https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#)

## Сборка и запуск проекта:
    git clone https://github.com/1ordhokage/chat-gpt-api

Из корневой папки проекта:

    docker-compose up -d 

Swagger: `http://0.0.0.0:8000/docs`

## Работа в Swagger:

При переходе на:
`http://0.0.0.0:8000/docs` будут доступны текущие эндпоинты. Для работы с некоторыми из них, требуется аутентификация/авторизация (такие эндпоинты помечены значком 🔓). 

- В правом верхнем углу есть кнопка `Authorize`, генерирующая форму для аутентификации.

- При успешной аутентификации, значки защищенных эндпоинтов меняются на 🔒, и теперь, вы можете тестировать защищенные эндпоинты (в заголовки запросов автоматически добаляется JWToken, сгенерированный на этапе аутентификации).


## Аутентификация:

JWT + Bearer

## Авторизация:

__user__:
 1) Может задавать вопросы Chat-GPT
 2) Может просмотреть список свои последних 3 вопросов
 3) Может увидеть данные о себе (без пароля)
 4) Может изменить данные о себе
 5) Удалить данные о себе (удалить аккаунт)

__admin__ может все то же самое, что и __user__, но еще:
 1) Может просматривать данные других пользователей (без пароля)
 2) Может просмотреть любой вопрос, зарегистрированный в системе


## Эндпоинты:

1) Регистрация.

    ```CURL
    curl -X 'POST' \
      'http://localhost:8000/auth/register' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "username": "string22",
      "text_password": "string22",
      "role": "admin"
    }'
    ```

    Пример ответа:

    Code 201
    ```JSON
    
    {
      "id": 4,
      "username": "string22",
      "role": "admin"
    }
    ```
2) Аутентификация
   
    ```CURL
    curl -X 'POST' \
      'http://localhost:8000/auth/token' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/x-www-form-urlencoded' \
      -d 'grant_type=&username=string22&password=string22&scope=&client_id=&client_secret='
    ```
    

   Пример ответа:

   Code 200
    ```JSON
    {
      "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDExODYzNzgsImV4cCI6MTcwMTE4OTk3OCwic3ViIjoiNCIsInJvbGUiOiJhZG1pbiJ9.Qwq_PlQW2peBLUjdWuyioZm5b7eHQDCpXispHyMCG4o",
      "token_type": "bearer"
    }
    

3) Вопрос Chat-GPT (🔓)

    ```CURL
    curl -X 'POST' \
      'http://localhost:8000/questions' \
      -H 'accept: application/json' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDExODQzNTYsImV4cCI6MTcwMTE4Nzk1Niwic3ViIjoiMiIsInJvbGUiOiJ1c2VyIn0.qXpBJOh6VVnD9CFk_VBtkqDLAZ-F2RDM7lnc5e1X9Xo' \
      -H 'Content-Type: application/json' \
      -d '{
      "content": "what is FastAPI"
    }'
    ```
    
   Пример ответа:

   Code 201
    ```JSON
    "FastAPI is a modern, fast (high-performance) web framework for building APIs with Python. It is built on top of Starlette for web routing and Pydantic for data validation and serialization. FastAPI is designed to be easy to use, efficient, and provide automatic interactive API documentation.\n\nSome key features of FastAPI include:\n\n1. Fast: It is based on asynchronous programming principles, which make it significantly faster than traditional web frameworks like Flask or Django. FastAPI supports high levels of concurrency, making it suitable for handling large amounts of traffic.\n\n2. Type-annotated: FastAPI utilizes type hints and type declarations to automatically generate interactive documentation, providing details about request and response models, request validation, and automatic serialization and deserialization of data.\n\n3. Automatic validation: With Pydantic, FastAPI is able to validate incoming requests against their expected models, automatically converting the request data into Python objects. If the validation fails, FastAPI will automatically return helpful validation error messages.\n\n4. Websockets and HTTP/2: FastAPI supports websockets and HTTP/2 out of the box, allowing for real-time communication and efficient data transfer.\n\n5. Authentication and authorization: FastAPI provides built-in support for various authentication methods, including OAuth2, JWT (JSON Web Tokens), and others. It also supports role-based and permission-based authorization.\n\n6. Dependency injection: FastAPI has built-in support for dependency injection, making it easy to manage and inject dependencies into your API functions.\n\nOverall, FastAPI is a powerful web framework that combines the ease of use and productivity of Flask with the performance benefits of asynchronous programming to provide an efficient and modern approach to building APIs in Python."
    ```

    
4) Получить вопрос по id (🔓 + admin)


    ```CURL
    curl -X 'GET' \
      'http://localhost:8000/questions?id=3' \
      -H 'accept: application/json' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDExODcwMTYsImV4cCI6MTcwMTE5MDYxNiwic3ViIjoiMSIsInJvbGUiOiJhZG1pbiJ9.UY5O-TaYYNUHXdUzIE6ZJXdyuNVeKZv-C41mmynWVjg'
    ```
    
    Пример ответа:

   Code 200
    ```JSON
        {
          "id": 3,
          "user_id": 1,
          "content": "what is capital of russia",
          "asked_at": "2023-11-28T14:02:54.681959"
        }
    ```

    
5) Получить список последних заданных трех вопросов (🔓)


    ```CURL
    curl -X 'GET' \
      'http://localhost:8000/questions/me' \
      -H 'accept: application/json' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDExODcwMTYsImV4cCI6MTcwMTE5MDYxNiwic3ViIjoiMSIsInJvbGUiOiJhZG1pbiJ9.UY5O-TaYYNUHXdUzIE6ZJXdyuNVeKZv-C41mmynWVjg'
    ```
    
    Пример ответа:

   Code 200
    ```JSON
        [
          {
            "id": 5,
            "user_id": 1,
            "content": "what is 2 times 2",
            "asked_at": "2023-11-28T15:04:22.362038"
          },
          {
            "id": 4,
            "user_id": 1,
            "content": "what is capital of russia",
            "asked_at": "2023-11-28T14:27:08.216508"
          },
          {
            "id": 3,
            "user_id": 1,
            "content": "what is capital of russia",
            "asked_at": "2023-11-28T14:02:54.681959"
          }
        ]
    ```
6) Получить информацию о пользователе по id (🔓 + admin)


    ```CURL
   curl -X 'GET' \
      'http://localhost:8000/users?id=2' \
      -H 'accept: application/json' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDExODcwMTYsImV4cCI6MTcwMTE5MDYxNiwic3ViIjoiMSIsInJvbGUiOiJhZG1pbiJ9.UY5O-TaYYNUHXdUzIE6ZJXdyuNVeKZv-C41mmynWVjg'
    ```
    
    Пример ответа:

   Code 200
    ```JSON
        {
          "id": 2,
          "username": "string11",
          "role": "user"
        }
    ```
    
7) Получить информацию о себе (🔓)


    ```CURL
   curl -X 'GET' \
      'http://localhost:8000/users/me' \
      -H 'accept: application/json' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDExODcwMTYsImV4cCI6MTcwMTE5MDYxNiwic3ViIjoiMSIsInJvbGUiOiJhZG1pbiJ9.UY5O-TaYYNUHXdUzIE6ZJXdyuNVeKZv-C41mmynWVjg'
    ```
    
    Пример ответа:

   Code 200
    ```JSON
        {
            "id": 1,
            "username": "string",
            "role": "admin"
        }
    ```



8) Обновить информацию о себе (🔓)


    ```CURL
   curl -X 'PUT' \
      'http://localhost:8000/users/me' \
      -H 'accept: */*' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDExODcwMTYsImV4cCI6MTcwMTE5MDYxNiwic3ViIjoiMSIsInJvbGUiOiJhZG1pbiJ9.UY5O-TaYYNUHXdUzIE6ZJXdyuNVeKZv-C41mmynWVjg' \
      -H 'Content-Type: application/json' \
      -d '{
      "username": "new_username",
      "text_password": "new_password"
    }'
    ```
    
    Пример ответа: Code 204

   

9) Удалить аккаунт (🔓)


    ```CURL
    curl -X 'DELETE' \
      'http://localhost:8000/users/me' \
      -H 'accept: */*' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDExODcwMTYsImV4cCI6MTcwMTE5MDYxNiwic3ViIjoiMSIsInJvbGUiOiJhZG1pbiJ9.UY5O-TaYYNUHXdUzIE6ZJXdyuNVeKZv-C41mmynWVjg'
    ```
    
    Пример ответа: Code 204

   







