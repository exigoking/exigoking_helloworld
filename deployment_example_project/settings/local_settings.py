DEBUG = False

DATABASES = {
    'default': {
        'NAME': 'exigoking_database_0001',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
        'PASSWORD': 'Iphone4S',
        'HOST': 'ec2-52-28-50-208.eu-central-1.compute.amazonaws.com',
        'PORT': '',
    },
}

ALLOWED_HOSTS = ["exigokinghelloworld", "ec2-52-28-54-11.eu-central-1.compute.amazonaws.com"]
