from django.conf import settings as st
from logging import ERROR

DEFAULT_AUTOMATED_LOGGING = {
    'exclude': ['Session', 'automated_logging'],
    'modules': ['request', 'model'],
    'to_database': True,
    'loglevel': {'model': ERROR,
                 'request': ERROR}
}


def auto_complete(setting, default):
  for k, v in default.items():
    if k not in setting.keys():
      setting[k] = v
    elif isinstance(setting[k], dict):
      setting[k] = auto_complete(setting[k], default[k])

  return setting


if hasattr(st, 'AUTOMATED_LOGGING'):
  AUTOMATED_LOGGING = auto_complete(st.AUTOMATED_LOGGING, DEFAULT_AUTOMATED_LOGGING)
else:
  AUTOMATED_LOGGING = DEFAULT_AUTOMATED_LOGGING


print(AUTOMATED_LOGGING)