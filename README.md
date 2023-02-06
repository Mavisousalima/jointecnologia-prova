# JoinTecnologia - [Prova][cult]

Crie um arquivo .env e adicione os campos abaixos com os dados do seu banco.

```
SECRET_KEY=YOUR_SECRET_KEY
DB_NAME=jointec_db
DB_USER=postgres
DB_PASSWORD=12345
DB_HOST=127.0.0.1
DB_PORT=5432
```

Para rodar a aplicação:

```
python manage.py makemigration
python manage.py migrate
python manage.py runserver
```

Para criar um superuser:

```
python manage.py createsuperuser
```

[cult]: http://cultofmartians.com/tasks/size-limit-config.html
