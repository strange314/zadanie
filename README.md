# 🔐 Full JWT Proxy Project: Django + FastAPI

Этот проект объединяет два сервиса — **Django** и **FastAPI**, работающих вместе через **JWT-аутентификацию**.  
Django управляет пользователями и выдает токены, а FastAPI запрашивает и проверяет эти токены перед выдачей публичных данных.

---

## 📁 Структура проекта
```bash
├── django_service/ # Django-приложение
│ ├── core/ # Конфигурация Django
│ ├── api/ # API endpoints (JWT + защита)
│ ├── manage.py # Запуск Django
│ ├── .env # Переменные окружения
│ └── requirements.txt # Зависимости Django
│
├── fastapi_service/ # FastAPI-приложение (прокси)
│ ├── main.py # Основной файл FastAPI
│ ├── .env # Переменные окружения
│ └── requirements.txt # Зависимости FastAPI
│
├── jwt_api_postman_collection.json # Коллекция Postman для тестирования
└── README.md # Документация проекта
```
---

## ⚙️ Установка и запуск

### 1. Django-сервис (`порт 8000`),  FastAPI-сервис (порт 8001)
```bash
cd zadanie/django_service
python -m venv venv
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8000
```

### 2.FastAPI-сервис (порт 8001)
```bash
cd /fastapi_service
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```
# 🔐 API Endpoints
## Django (порт 8000)
| Метод | Endpoint               | Описание                                |
| ----- | ---------------------- | --------------------------------------- |
| POST  | `/api/gen-token/`      | Получить JWT по `username` и `password` |
| GET   | `/api/protected-data/` | Защищённый эндпоинт, требует токен      |

## Пример запроса на получение токена:
```bash
POST http://localhost:8000/api/gen-token/
```
```bash
{
  "username": "admin",
  "password": "your_password"
}
```
## FastAPI (порт 8001)
Пример запроса
```bash
GET http://localhost:8001/public-data/
Authorization: Bearer <ваш_access_token>
```
```bash
{
  "data": "some public data",
  "user": "admin"
}
```
