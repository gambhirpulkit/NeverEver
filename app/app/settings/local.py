from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)

#ALLOWED_HOSTS = [127.0.0.1]

SECRET_KEY = env('DJANGO_SECRET_KEY', default='lx9joase75e!kb+8*2=z6vs!a+@)c2q*hbhwpb9&0kv31et%ac')