## 1.2.3 (06.05.24)
    - Исправлено добаление аналога в бд(корректное наименование артикула и производителя)
## 1.2.1 (05.05.24)
    - Исправлен поиск в панели администраторв (ManufacturerAdmin)
## 1.2.0 (01.05.24)
    - Добавлено приложение для работы с доставкой
## 1.1.0 (01.05.24)
    - Добавлен скрипт для скачивания дампа и обновения БД
## 1.0.57 (27.04.24)
    - Поиск по артикулу
## 1.0.56 (26.04.24)
    - Оптимизация результатов поиска
## 1.0.55 (22.04.24)
    - Фиды без изображений
    - Наценка для Авито
## 1.0.54 (19.04.24)
    - Сбор предложений круглосуточно
## 1.0.53 (17.04.24)
    - Служебные изображения
    - Кеш для количества предложений
## 1.0.52 (16.04.24)
    - Сборщик для предложений
    - Формирование фида для рекламы
## 1.0.51 (08.04.24)
    - Фильтр через стоп слова
## 1.0.50 (04.04.24)
    - Сборщик аналогов и ссылок на изображения
## 1.0.49 (01.04.24)
    - Структура для справочника
## 1.0.48 (20.03.24)
    - Добавил таймаут для Автоевро
## 1.0.47 (19.03.24)
    - Кнопка "Помощь в подборе" явная на главной странице
    - Добавил город по умолчанию (Оренбург)
    - Убрал сервисный сбор
    - Добавил таймер-гифку для ожидания закрузки
## 1.0.46 (07.03.24)
    - Ускорил результаты поиска
## 1.0.45 (04.03.24)
    - Добавлен sitemap.xml отдельным файлом
## 1.0.44 (01.03.24)
    - Сообщения для помощи в подборе в форме
    - Переадресация после помощи в подборе
    - Предложение добавить вин номер в гараж на главной странице
    - Переадресация после авторизации
    - Проверка вин номера в бд
## 1.0.43 (29.02.24)``
    - Добавлена помощь в подборе
## 1.0.42 (27.02.24)
    - Исправлены искомые артикулы для автотрейда
## 1.0.41 (26.02.24)
    - Добавлены адреса для складов Армтека
    - Добавлен тестовый yandex-feed
    - Добавлен версия питон в README.md
## 1.0.40 (21.02.24)
    - Исправил вывод запрашиваемых деталей для парткома
## 1.0.39
    - Добавлены артикулы из Армтека при запросе ...v0/search-results/ (SearchResulsAPI)

## 1.0.38 (16.02.24)
    - Обновлена логика для доставки. (Один поставщик - одна доставка)
    - Добавлена корзина в бургер меню если пользователь неавторизован
## 1.0.37 (12.02.24)
    - Добавлены адреса складов для поставщиков
    - Добавлен ссылка на бота продавца для помощи в подборе детали

## 1.0.36 (12.02.24)
    - ПРИНЯЛИ ПЕРВУЮ РЕАЛЬНУЮ ОПЛАТУ!!!

## 1.0.35 (9.02.24)
    - Добавлен новый блок к предложениями для запрашиваемого артикула с доставкой
    - Добавлена пагинация и сортировка для блока с предложениями с запрашиваемым артиркулом с доставкой
## 1.0.34 (7.02.24)
    - Есть сортировка по времени доставки и цене
## 1.0.33 (6.02.24)
    - Есть формирование ссылки(артикул+бренд) в гугл для поиска изображения товара
## 1.0.32 (5.02.24)
    - Есть получение предложений от поставщиков с их партнерами
## 1.0.31 (2.02.24)
    - Есть гугл аналитика на сайте
## 1.0.30 (1.02.24)
    - Автотрейд подключен как поставщик
    - Есть получение паспорта для оформления доверенности
## 1.0.29 (19.01.24)
    - Армтек подключен как поставщик
    - Есть добавление паспорта
    - Есть хеширование паспорта
    - Есть стоимость доставки по умолчанию
    - Есть сервисный сбор
    - Есть наценка для предложения
## 1.0.28 (10.01.24)
    - Ожидание оплаты втечении 24 часов
    - Заявка на отмену заказа на почту
    - Добавлена стоимость доставки по умолчанию (300 р)
    - Формирование чека
## 1.0.27 (9.01.24)
    - (!!!) Оплата заказов на сайте


## 1.0.26 (22.12.23)
    - Есть асинхронность через uvicorn и asyncio
## 1.0.26 (14.12.23)
    - Есть асинхронность (получает предложения от разных поставщиков)
## 1.0.25
    - Автоевро подключен как поставщик
    - Партком подключен как поставщик
    - Есть вывод предложений от Автоевро на сайте
    - Есть пагинация для предложений в наличии и аналогов
## 1.0.24
    - Есть разделение для получения сообщений: в группе или в личном чате
    - Есть вывод телеграм фрейма в браузере
## 1.0.23
    - Есть диалог в телеграме для выбора модели
    - Есть добавление в кеш ссылки для модели
    - Есть кнока "Назад" для навигации по каталогам
## 1.0.22
    - Есть функционал работы с командами Корзина, Заказы, Каталоги, Регистрация, Помощь через бота
## 1.0.21
    - Есть открытие сайт во фрейме через бота
## 1.0.20
    - Есть анимированная пагинация
## 1.0.19
    - Есть заполнение групп для админов
    - Есть регистрация админов по ключу
## 1.0.18
    - Добавлена ссылка на изображение для товара
## 1.0.17
    - Есть сохранение корзины в куки браузера для НЕавторизованного пользователя
## 1.0.16
    - Есть повторная проценка корзины
## 1.0.15
    - Лимит запросов в час для каталога оригиальных запчастей вынесен 
    в settings (CATALOG_LIMIT) и увеличен до 200 по умолчанию
## 1.0.14.1
    - Логирование для оплаты
## 1.0.14
    - Добавлен title "Время доставки" в иконку доcтавка в разультатах поиска
    - Добавлен скрипт восстановления БД
    - Исправлена опечатка
    - Обновлен gitignore
    - Обновлен строковый вид заказа в админке
    - Добавлены фильтры в адиминке для заказов и доставок
## 1.0.13
    - Уменьшен таймаут при рендере товарных предложений.
## 1.0.12
    - Добавлены ссылки на страницу "Заказы".
## 1.0.11 (19.07.2023)
    - Есть корзина.
## 1.0.10 (21.06.2023)
    - Есть Sitemap и robots.txt.
## 1.0.10 (26.05.2023)
    - Есть предварительный расчет стоимости доставки от яндекса.
    - Есть отправка данных для формирование доставки на телеграм и емейл.
## 1.0.9
    - Есть подсчет доставки.
## 1.0.8
    - Есть вывод марок и моделей от acat.
## 1.0.7
    - Есть вывод предложений от docpart.
    - Есть вывод интеграция с docpart.
    - Есть вывод подсказок адресов от dadata.
## 1.0.6
    - Есть вывод предложений для запрашиваемых артикулов и аналогов.
    - Есть вывод таблицы предложений с доставкой.
## 1.0.5
    - Добавлены 2 телеграм бота для покупателей и продавцов.
    - Покупатель может оставлять и удалять завки.
    - Продавец может реагировать на заяки и удалять их.
## 1.0.4
    - Подключен сайт drandulet.net как магазин на геозипе.
    - Все логи пишутся в файл "debug.log".
    - Есть вывод предложений из бд.
## 1.0.3
    - Есть отправка предложений на емейл.
    - Есть востановление пароля.
## 1.0.2
    - Обновлен AUTORUS_URL.
## 1.0.1
    - Добавлена возможность добавления страниц в футер.
## 1.0.0
    - Работает регистрация, доавбление и поик товаров.
