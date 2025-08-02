# 🔐 Full JWT Proxy Project: Django + FastAPI

Этот проект объединяет два сервиса — **Django** и **FastAPI**, работающих вместе через **JWT-аутентификацию**.  
Django управляет пользователями и выдает токены, а FastAPI запрашивает и проверяет эти токены перед выдачей публичных данных.

---

## 📁 Структура проекта


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
