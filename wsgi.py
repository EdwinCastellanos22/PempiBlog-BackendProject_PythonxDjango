import os
import sys

path= '/home/pempi2022/blog'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE']= 'blog.settings'

from django.core.wsgi import get_wsgi_application
application= get_wsgi_application()