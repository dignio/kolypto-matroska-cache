from importlib.metadata import version

__version__ = version('matroska-cache')


from .cache import MatroskaCache
from .exc import NotInCache
from . import dep

try:
    from .sa_tools import sa_dependencies, sa_modified_names
except ImportError:
    pass
