from common.utils import get_env

DEBUG = get_env('FLASK_DEBUG', True)
ENV = get_env('FLASK_ENV', 'development')

HOST = get_env('HOST', '0.0.0.0')
PORT = get_env('PORT', 5002)
