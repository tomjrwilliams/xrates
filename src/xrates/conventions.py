
from __future__ import annotations

import enum

import xtuples as xt

# ---------------------------------------------------------------

class Overflow(enum.Enum):
    ERROR = 0
    PREV = -1
    NEXT = 1

# ---------------------------------------------------------------

class Roll(enum.Enum):
    ERROR = 0
    PRECEDING = -1
    FOLLOWING = 1

class Modified(enum.Enum):
    UNMODIFIED = 0
    MODIFIED = 1

# ---------------------------------------------------------------

class Format(enum.Enum):
    ISO = 0
    
# ---------------------------------------------------------------

DAY_COUNTS = xt.iTuple([
    "SIMPLE",

    "ACTUAL_365_F",
    "ACTUAL_360",
    "ACTUAL_364",
    "ACTUAL_ACTUAL_ICMA",
    "ACTUAL_365_L",
    "ACTUAL_ACTUAL_ISDA",
    "ACTUAL_ACTUAL_AFB",

    "N_30_360_BOND",
    "N_30_360_US",
    "N_30E_360",
    "N_30E_360_ISDA",
    "N_30E_PLUS_360",

    "N_1_1",
])
Day_Count = enum.Enum("Day_Count", DAY_COUNTS)

# ---------------------------------------------------------------

