# Приложение для LMS-системы, в которой каждый желающий может размещать свои полезные материалы или курсы.
Для запуска установите зависимости из файла [requirements.txt](requirements.txt) и заполните шаблон [.env.sample](.env.sample)

## 1. Создан новый Django-проект, подключен DRF в настройках проекта.
## 2. Созданы следующие модели:

Пользователь:
все поля от обычного пользователя, но авторизацию заменить на email;
телефон;
город;
аватарка.
Модель пользователя разместите в приложении users

•Курс:

название,
превью (картинка),
описание.

•Урок:

название,
описание,
превью (картинка),
ссылка на видео.

## 3. Описан CRUD для моделей курса и урока. Для реализации CRUD для курса использован Viewsets, а для урока - Generic-классы.
## 4. Для модели курса добавлен в сериализатор поле вывода количества уроков.
## 5. Описана новая модель для платежей в приложении "users"
## 6. Добавлена фильтрация для списка платежей
