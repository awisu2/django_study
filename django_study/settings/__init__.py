from os import getenv

try:
    MODE = getenv('MODE')
    if MODE == 'production':
        from .prod import *
    else:
        from .dev import *

except Exception as e:
    print(e)


