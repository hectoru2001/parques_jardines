import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parques_jardines.settings')
application = get_wsgi_application()
