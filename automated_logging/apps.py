from django.apps import AppConfig
from .settings import settings


class AutomatedloggingConfig(AppConfig):
    name = 'automated_logging'
    verbose_name = 'Django Automated Logging (DAL)'

    def ready(self):
        if 'request' in settings.modules:
            from .signals import request # noqa
        if 'model' in settings.modules:
            from .signals import save # noqa
            from .signals import m2m # noqa

        from .signals import common # noqa
        from .handlers import DatabaseHandler # noqa
