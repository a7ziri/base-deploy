# Text Classifier API

Простой API на FastAPI для классификации можно  использовать как шаблон  при  созлании  прототипов

Endpoints:

*   **Классификация текста:** Эндпоинт `/classify` принимает текст и возвращает предсказание тональности (например, POSITIVE/NEGATIVE).
*   **Проверка статуса:** Эндпоинт `/status` возвращает текущий статус API и используемую модель.
*   **Аутентификация:** Простая проверка токена для доступа к эндпоинту `/classify`.

Технологии

*   [FastAPI](https://fastapi.tiangolo.com/) - Веб-фреймворк
*   [Transformers](https://huggingface.co/transformers/) - Библиотека для работы с state-of-the-art моделями машинного обучения
*   [Pydantic](https://pydantic-docs.helpmanual.io/) - Валидация данных
*   [Uvicorn](https://www.uvicorn.org/) - ASGI сервер
*   [python-dotenv](https://github.com/theskumar/python-dotenv) - Загрузка переменных окружения

Установка

1.  **Клонируйте репозиторий (если применимо):**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2.  **Создайте и активируйте виртуальное окружение (рекомендуется):**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Установите зависимости:**
    Создайте файл `requirements.txt` (если его еще нет) со следующим содержимым:
    ```txt
    fastapi
    transformers[torch] # Или transformers[tensorflow], если вы используете TensorFlow
    uvicorn[standard]
    python-dotenv
    ```
    Затем выполните команду:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Настройте переменные окружения:**
    Создайте файл `.env` в корне проекта и добавьте секретный токен:
    ```
    SECRET_TOKEN=your_secret_token_here
    ```
    Замените `your_secret_token_here` на ваш собственный секретный токен.

Запуск API

Выполните следующую команду в терминале, находясь в корневой директории проекта:

```bash
uvicorn main:app --reload
```

Сервер будет доступен по адресу `http://localhost:8000`.

окументация API (Swagger UI)

Автоматически сгенерированная интерактивная документация доступна по адресу `http://localhost:8000/docs` после запуска сервера.
