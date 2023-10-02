
import os
import sys
import pathlib

if pathlib.Path(os.getcwd()).parts[-1] == "xrates":
    sys.path.append("./__local__")

    import PATHS

    if PATHS.XTUPLES not in sys.path:
        sys.path.append(PATHS.XTUPLES)
        print(sys.path)

    if PATHS.XTENORS not in sys.path:
        sys.path.append(PATHS.XTENORS)
        print(sys.path)

from . import conventions
from . import counts
from . import schedules

from .xrates import *