# Blog-with-admin
Blog with user management made in Django

## How to run the project locally
### Requiremnts:
- A virtual environment, you can create it with ```$ python3 -m venv env``` and activate it with ```$ source env/bin/activate```
- Depending on your taste, you'll may want to use ```sqlite3``` database or you'll may want to use ```PostgreSQL```

### With Sqlite3
If you want to use this db, then go to the folder called blog and inside that folder you should see a file structure like the following:
```blog/blog/settings.py``` open the settings.py file and then comment these lines: 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbmam6qalmegsc',
        'USER': os.environ['pguser'],
        'PASSWORD': os.environ['pgpassword'],
        'HOST': os.environ['pghost'],
        'PORT': os.environ['pgport']

    }
}
```

### With postgreSQL
If you want to use this db, then go to the folder called blog and inside that folder you should see a file structure like the following:
```blog/blog/settings.py``` open the settings.py file and then comment these lines: 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

If you chosed to go with this option then you're going to need to create a few environment variables:
- ```pguser```
- ```pgpassword```
- ```pghost```
- ```pgport```

Fill those environment variables with your own settings

## How to run the project (windows)
Create a virtual environment (windows)
In a new powershell navigate to the project folder and run
```powershell
py -m venv env
```

Activate the environment
```
env\Scripts\activate
```

Install the requirements
```powershell
pip install -r requirements.txt
```

Migrate the db
```powershell
py manage.py makemigrations
py manage.py migrate --run-syncdb
```

Start the development server
```powershell
py manage.py runserver
```

## How to run the project (linux)
Create a virtual environment (linux)
In a new powershell navigate to the project folder and run
```bash
python3 -m venv env
```

Activate the environment
```bash
source env/bin/activate
```

Install the requirements
```bash
pip install -r requirements.txt
```

Migrate the db
```bash
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
```

Start the development server
```bash
python3 manage.py runserver
```