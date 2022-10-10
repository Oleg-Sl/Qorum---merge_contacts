import os
import json
from django.conf import settings


filename_secrets_django = os.path.join(settings.BASE_DIR, 'django_secrets.json')


def get_secret_django(key):
    with open(filename_secrets_django) as secrets_file:
        data = json.load(secrets_file)

    return data.get(key)
