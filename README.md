# geozip

## Python
python version: 3.9.2


## Proxmox
192.168.1.99:8006

## Настройка ubuntu server 20.04:
### Настройка сети

>sudo nano /etc/netplan/00-installer-config.yaml

```
network:
  ethernets:
    ens18:
      addresses:
        - 192.168.1.102/24
      gateway4: 192.168.1.1
      nameservers:
        addresses: [192.168.1.1, 8.8.8.8, 8.8.8.4]
      optional: true
      dhcp4: false
  version: 2
```

sudo netplan generate
sudo netplan apply

### Настройка postgresql

```
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo -i -u postgres
psql
CREATE USER gz WITH PASSWORD '****';
CREATE DATABASE gz
  WITH OWNER = gz
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'ru_RU.UTF-8'
       LC_CTYPE = 'ru_RU.UTF-8'
       CONNECTION LIMIT = -1;
GRANT CONNECT, TEMPORARY ON DATABASE gz TO public;
GRANT ALL ON DATABASE gz TO postgres;
GRANT ALL ON DATABASE gz TO gz;
```




### Установка pyenv

>sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
>libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
>libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl


>sudo cd /usr/local/src && curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

>sudo nano ~/.bashrc
```
export PYENV_ROOT="${HOME}/.pyenv"

if [ -d "${PYENV_ROOT}" ]; then
    export PATH="${PYENV_ROOT}/bin:${PATH}"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
fi
```
>source ~/.bashrc


### Настройка pyenv
```
>pyenv versions
>pyenv install 3.9.2
>pyenv local 3.9.2
>pyenv virtualenv 3.9.2 gz 
>pyenv activate gz
```

### Настройка безопасности - Fail2Ban
```
apt install fail2ban
nano /etc/fail2ban/jail.conf
bantime - количество секунд на которые будет блокироваться злоумышленник) 
maxretry (количество попыток ввода логина/пароля) для каждого отдельного сервиса.
systemctl restart fail2ban
```
### PostgreSQL
#### Установка:
>sudo apt-get update

>sudo apt-get install postgresql postgresql-contrib

#### Проверка
>sudo -i -u postgres             # вход в аккаунт
или
>sudo -u postgres psql           # интерфейс программной строки Postgres

\q                              # выход

#### Создать юзера:
>sudo -i -u postgres
или
>createuser --interactive
name


#### Создать БД:
sudo -i -u postgres
createdb blizkodb
или
sudo -u postgres createdb blizkodb

sudo adduser ***

#### Дать права на создание баз данных:
ALTER USER blizko CREATEDB;

### Открыть доступ к БД с внешки
sudo nano /etc/postgresql/12/main/postgresql.conf 
listen_addresses = '*' или  listen_addresses = '192.168.1.101'

sudo nano /etc/postgresql/12/main/pg_hba.conf 
внизу добавить
host     all     all     192.168.0.10/32     password

systemctl restart postgresql

#Список url-ов.
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

Proxmox: root@192.168.1.99
Сервер БД: gz@192.168.1.102
geozip.ru: gz@192.168.1.101


### Работа с Loguru
- добавить необходимый путь к log файлу
LOGURU_FILE = '***'

### Для запуска проетка
pip install virtualenv  # устанавливает виртуальное окружение

cd в корневую директорию

python -m venv venv  # создает виртуальное окружение

source venv/bin/activate  # запускает виртуальное окружение(linux, mac)

pip install wheel #

pip install -r back/requirements/base.txt  # устанавливает зависимости

### Команды основные
python manage.py runserver  # запускает проект

python manage.py makemigrations  # создает миграции

python manage.py migrate  # создает таблицы в бд

python manage.py collectstatic  # переносит статику в static
### Команды /managment/commands
python manage.py acat_brands  # добавляет типы марок и марки автомобилей из acat

python manage.py acat_models  # добавляет модели автомобилей из acat

python manage.py city  # добавляет города и регионы

python manage.py brands  # добавляет бренды товаров

python manage.py products  # добавляет товары и артикулы


### Инструкции для redis
https://www.dmosk.ru/miniinstruktions.php?mini=redis-ubuntu
