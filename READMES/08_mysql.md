# 08_mysql

```bash
pip -m pip install -U pip
pip install mysqlclient

# ----- settings.py >>>>>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_study',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '192.168.99.100', # default: localhost
        'PORT': '', # default: 3306
    }
}
# ----- settings.py <<<<<

python manage.py migrate
```
