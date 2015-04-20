# application_python cookbook expects manage.py in a top level
# instead of app level dir, so the relative import can fail
try:
    from .exigoking_helloworld.exigoking_helloworld.settings.base import *
except ImportError:
    from exigoking_helloworld.settings.base import *


try:
    from local_settings import *
except ImportError:
    pass
