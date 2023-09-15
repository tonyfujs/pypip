# read version from installed package
from importlib.metadata import version
from .pip import build_request
from .utils import health_check
__version__ = version("pypip")


