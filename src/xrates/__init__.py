
import os
import sys
import pathlib

import os
import sys

sys.path.append("./__local__")
sys.path.append("./src")

sys.path.append(os.environ["xtuples"])
sys.path.append(os.environ["xtenors"])

from . import conventions
from . import counts
from . import schedules

from .xrates import *