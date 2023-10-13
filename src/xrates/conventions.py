
from __future__ import annotations

import enum

import xtuples as xt
    
# ---------------------------------------------------------------

class Day_Count(enum.Enum):
    SIMPLE = "SIMPLE"

    ACTUAL_365_F = "ACTUAL_365_F"
    ACTUAL_360 = "ACTUAL_360"
    ACTUAL_364 = "ACTUAL_364"
    ACTUAL_ACTUAL_ICMA = "ACTUAL_ACTUAL_ICMA"
    ACTUAL_365_L = "ACTUAL_365_L"
    ACTUAL_ACTUAL_ISDA = "ACTUAL_ACTUAL_ISDA"
    ACTUAL_ACTUAL_AFB = "ACTUAL_ACTUAL_AFB"

    N_30_360_BOND = "N_30_360_BOND"
    N_30_360_US = "N_30_360_US"
    N_30E_360 = "N_30E_360"
    N_30E_360_ISDA = "N_30E_360_ISDA"
    N_30E_PLUS_360 = "N_30E_PLUS_360"

    N_1_1 = "N_1_1"


# ---------------------------------------------------------------

