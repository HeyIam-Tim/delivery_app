Установка:
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

Проверка
sudo -i -u postgres             # вход в аккаунт
или
sudo -u postgres psql           # интерфейс программной строки Postgres

\q                              # выход

Создать юзера:
sudo -i -u postgres
или
createuser --interactive
name


Создать БД:
sudo -i -u postgres
createdb blizkodb
или
sudo -u postgres createdb blizkodb

sudo adduser ***

Дать права на создание баз данных:
ALTER USER blizko CREATEDB;


Список url-ов.
- Незарегистрированные пользователи:
  /                           # Главная страница.
  /products/{productId}/      # Страница с продуктом.
  /categories/                # Страница с категориями товаров.
  
- Зарегистрированные пользователи:
  /profile/login/             # Логин страница.
  /profile/register/          # Регистрация.
  /profile/reset-password/    # Востановление пароля.
  /profile/                   # Личный кабинет магазина.
  /profile/shops/             # Страница с магазинами.
  
- APIs:
 

