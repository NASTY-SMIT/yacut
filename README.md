# "Укоротитель ссылок YaCut"
## Проект YaCut — это сервис укорачивания ссылок. 
### Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.
## С помощью проекта можно:
- Работать с api по адресу http://127.0.0.1:5000/api/id/
- Создать свою кастомную ссылку по адресу http://127.0.0.1:5000/
- Ваша кастомная ссылка будет автоматически переадресовывать на оригинальную ссылку
### Используемые технологии
- Python 3.9
- Flask
- SQLAlchemy
- REST API

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:NASTY-SMIT/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
## Как работать с Yacut

```
flask run
```
❤️Автор [Nasty Shmidt](https://github.com/NASTY-SMIT)❤️
[Telegram](https://t.me/nastyShmidt)