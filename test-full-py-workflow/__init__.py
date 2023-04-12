from . import config

CONFIG = config.ConfigManager()

from pkg_resources import get_distribution

__version__ = get_distribution("test-full-py-workflow").version
