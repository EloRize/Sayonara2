# Sayonara

Пример веб-проекта на FastAPI и React (Vite). Проект содержит минимальный набор API и компонентов.

## Запуск backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn openpyxl
uvicorn app.main:app --reload
```

## Запуск frontend

```bash
cd frontend
npm install
npm run dev
```

Функционал работы с Excel реализован через библиотеку `openpyxl`. Формулы и форматирование сохраняются при сохранении файла.
