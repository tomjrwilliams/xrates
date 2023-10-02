

import datetime

from financepy.utils.frequency import FrequencyTypes
from financepy.utils.day_count import DayCount, DayCountTypes
from financepy.utils.date import Date as Date

import xtuples as xt
import xrates as xr

import xtenors as tenors

from . import utils

# ---------------------------------------------------------------

# round(answer[0], 4) == 0.3889
def year_frac_30_360_bond_financepy(
    start = Date(1, 1, 2019),
    end = Date(21, 5, 2019),
):
    def f():
        finFreq = FrequencyTypes.ANNUAL
        day_count_type = DayCountTypes.THIRTY_360_BOND
        day_count = DayCount(day_count_type)
        return day_count.year_frac(start, end, end, finFreq)[0]
    f.__name__ = utils.outer_func_name()
    return f 

def year_frac_30_360_bond_xtenors_py(
    start = datetime.date(2019, 1, 1),
    end = datetime.date(2019, 5, 21),
):
    def f():
        return xr.counts.day_factor_py(
            start,
            end,
            end,
            freq=1,
            count=xr.conventions.Day_Count.N_30_360_BOND,
        )
    f.__name__ = utils.outer_func_name()
    return f

def year_frac_30_360_bond_xtenors_C(
    start = datetime.date(2019, 1, 1),
    end = datetime.date(2019, 5, 21),
):
    def f():
        return xr.counts.day_factor_C(
            start,
            end,
            end,
            freq=1,
            count=xr.conventions.Day_Count.N_30_360_BOND,
        )
    f.__name__ = utils.outer_func_name()
    return f

# ---------------------------------------------------------------

# round(answer[0], 4) == 0.3889
def year_frac_30E_360_financepy(
    start = Date(1, 1, 2019),
    end = Date(21, 5, 2019),
):
    def f():
        finFreq = FrequencyTypes.ANNUAL
        day_count_type = DayCountTypes.THIRTY_E_360
        day_count = DayCount(day_count_type)
        return day_count.year_frac(start, end, end, finFreq)[0]
    f.__name__ = utils.outer_func_name()
    return f 

def year_frac_30E_360_xtenors_py(
    start = datetime.date(2019, 1, 1),
    end = datetime.date(2019, 5, 21),
):
    def f():
        return xr.counts.day_factor(
            start,
            end,
            end,
            freq=1,
            count=xr.conventions.Day_Count.N_30E_360,
        )
    f.__name__ = utils.outer_func_name()
    return f

# ---------------------------------------------------------------

# round(answer[0], 4) == 0.3889
def year_frac_30E_360_isda_financepy(
    start = Date(1, 1, 2019),
    end = Date(21, 5, 2019),
):
    def f():
        finFreq = FrequencyTypes.ANNUAL
        day_count_type = DayCountTypes.THIRTY_E_360_ISDA
        day_count = DayCount(day_count_type)
        return day_count.year_frac(start, end, end, finFreq)[0]
    f.__name__ = utils.outer_func_name()
    return f 

def year_frac_30E_360_isda_xtenors_py(
    start = datetime.date(2019, 1, 1),
    end = datetime.date(2019, 5, 21),
):
    def f():
        return xr.counts.day_factor(
            start,
            end,
            end,
            freq=1,
            count=xr.conventions.Day_Count.N_30E_360_ISDA,
        )
    f.__name__ = utils.outer_func_name()
    return f

# ---------------------------------------------------------------

# round(answer[0], 4) == 0.3889
def year_frac_30E_plus_360_financepy(
    start = Date(1, 1, 2019),
    end = Date(21, 5, 2019),
):
    def f():
        finFreq = FrequencyTypes.ANNUAL
        day_count_type = DayCountTypes.THIRTY_E_PLUS_360
        day_count = DayCount(day_count_type)
        return day_count.year_frac(start, end, end, finFreq)[0]
    f.__name__ = utils.outer_func_name()
    return f 

def year_frac_30E_plus_360_xtenors_py(
    start = datetime.date(2019, 1, 1),
    end = datetime.date(2019, 5, 21),
):
    def f():
        return xr.counts.day_factor(
            start,
            end,
            end,
            freq=1,
            count=xr.conventions.Day_Count.N_30E_PLUS_360,
        )
    f.__name__ = utils.outer_func_name()
    return f

# ---------------------------------------------------------------

# assert round(answer[0], 4) == 0.3836
def year_frac_act_act_isda_financepy(
    start = Date(1, 1, 2019),
    end = Date(21, 5, 2019),
):
    def f():
        finFreq = FrequencyTypes.ANNUAL
        day_count_type = DayCountTypes.ACT_ACT_ISDA
        day_count = DayCount(day_count_type)
        return day_count.year_frac(start, end, end, finFreq)[0]
    f.__name__ = utils.outer_func_name()
    return f 

def year_frac_act_act_isda_xtenors_py(
    start = datetime.date(2019, 1, 1),
    end = datetime.date(2019, 5, 21),
):
    def f():
        return xr.counts.day_factor(
            start,
            end,
            end,
            freq=1,
            count=xr.conventions.Day_Count.ACTUAL_ACTUAL_ISDA,
        )
    f.__name__ = utils.outer_func_name()
    return f

# ---------------------------------------------------------------

# assert round(answer[0], 4) == 1.0000
def year_frac_act_act_icma_financepy(
    start = Date(1, 1, 2019),
    end = Date(21, 5, 2019),
):
    def f():
        finFreq = FrequencyTypes.ANNUAL
        day_count_type = DayCountTypes.ACT_ACT_ICMA
        day_count = DayCount(day_count_type)
        return day_count.year_frac(start, end, end, finFreq)[0]
    f.__name__ = utils.outer_func_name()
    return f 

def year_frac_act_act_icma_xtenors_py(
    start = datetime.date(2019, 1, 1),
    end = datetime.date(2019, 5, 21),
):
    def f():
        return xr.counts.day_factor(
            start,
            end,
            end,
            freq=1,
            count=xr.conventions.Day_Count.ACTUAL_ACTUAL_ICMA,
        )
    f.__name__ = utils.outer_func_name()
    return f

# ---------------------------------------------------------------

# assert round(answer[0], 4) == 0.3836
def year_frac_act_365_f_financepy(
    start = Date(1, 1, 2019),
    end = Date(21, 5, 2019),
):
    def f():
        finFreq = FrequencyTypes.ANNUAL
        day_count_type = DayCountTypes.ACT_365F
        day_count = DayCount(day_count_type)
        return day_count.year_frac(start, end, end, finFreq)[0]
    f.__name__ = utils.outer_func_name()
    return f 

def year_frac_act_365_f_xtenors_py(
    start = datetime.date(2019, 1, 1),
    end = datetime.date(2019, 5, 21),
):
    def f():
        return xr.counts.day_factor(
            start,
            end,
            end,
            freq=1,
            count=xr.conventions.Day_Count.ACTUAL_365_F,
        )
    f.__name__ = utils.outer_func_name()
    return f

# ---------------------------------------------------------------

# round(answer[0], 4) == 0.3889
def year_frac_act_360_financepy(
    start = Date(1, 1, 2019),
    end = Date(21, 5, 2019),
):
    def f():
        finFreq = FrequencyTypes.ANNUAL
        day_count_type = DayCountTypes.ACT_360
        day_count = DayCount(day_count_type)
        return day_count.year_frac(start, end, end, finFreq)[0]
    f.__name__ = utils.outer_func_name()
    return f 

def year_frac_act_360_xtenors_py(
    start = datetime.date(2019, 1, 1),
    end = datetime.date(2019, 5, 21),
):
    def f():
        return xr.counts.day_factor(
            start,
            end,
            end,
            freq=1,
            count=xr.conventions.Day_Count.ACTUAL_360,
        )
    f.__name__ = utils.outer_func_name()
    return f

# ---------------------------------------------------------------

# assert round(answer[0], 4) == 0.3836
def year_frac_act_365_l_financepy(
    start = Date(1, 1, 2019),
    end = Date(21, 5, 2019),
):
    def f():
        finFreq = FrequencyTypes.ANNUAL
        day_count_type = DayCountTypes.ACT_365L
        day_count = DayCount(day_count_type)
        return day_count.year_frac(start, end, end, finFreq)[0]
    f.__name__ = utils.outer_func_name()
    return f 

def year_frac_act_365_l_xtenors_py(
    start = datetime.date(2019, 1, 1),
    end = datetime.date(2019, 5, 21),
):
    def f():
        return xr.counts.day_factor(
            start,
            end,
            end,
            freq=1,
            count=xr.conventions.Day_Count.ACTUAL_365_L,
        )
    f.__name__ = utils.outer_func_name()
    return f

# ---------------------------------------------------------------

# round(answer[0], 4) == 0.3836
def year_frac_simple_financepy(
    start = Date(1, 1, 2019),
    end = Date(21, 5, 2019),
):
    def f():
        finFreq = FrequencyTypes.ANNUAL
        day_count_type = DayCountTypes.SIMPLE
        day_count = DayCount(day_count_type)
        return day_count.year_frac(start, end, end, finFreq)[0]
    f.__name__ = utils.outer_func_name()
    return f 

def year_frac_simple_xtenors_py(
    start = datetime.date(2019, 1, 1),
    end = datetime.date(2019, 5, 21),
):
    def f():
        return xr.counts.day_factor(
            start,
            end,
            end,
            freq=1,
            count=xr.conventions.Day_Count.SIMPLE,
        )
    f.__name__ = utils.outer_func_name()
    return f

# ---------------------------------------------------------------

def test_day_counts():
    print(":")
    
    utils.compare(
        year_frac_30_360_bond_xtenors_py(), 
        year_frac_30_360_bond_xtenors_C(),
        iters=10 ** 6
    )
    utils.compare(
        year_frac_30_360_bond_financepy(), 
        year_frac_30_360_bond_xtenors_C(), 
        fastest=1,
    )
    
    utils.compare(
        year_frac_30E_360_financepy(),
        year_frac_30E_360_xtenors_py(),
        fastest=1,
    )
    utils.compare(
        year_frac_30E_360_isda_financepy(),
        year_frac_30E_360_isda_xtenors_py(),
        fastest=1,
    )
    utils.compare(
        year_frac_30E_plus_360_financepy(),
        year_frac_30E_plus_360_xtenors_py(),
        fastest=1,
    )
    utils.compare(
        year_frac_act_act_isda_financepy(),
        year_frac_act_act_isda_xtenors_py(),
        fastest=1,
    )
    utils.compare(
        year_frac_act_act_icma_financepy(),
        year_frac_act_act_icma_xtenors_py(),
        fastest=1,
    )
    utils.compare(
        year_frac_act_365_f_financepy(),
        year_frac_act_365_f_xtenors_py(),
        fastest=1,
    )
    utils.compare(
        year_frac_act_360_financepy(),
        year_frac_act_360_xtenors_py(),
        fastest=1,
    )
    utils.compare(
        year_frac_act_365_l_financepy(),
        year_frac_act_365_l_xtenors_py(),
        fastest=1,
    )
    utils.compare(
        year_frac_simple_financepy(),
        year_frac_simple_xtenors_py(),
        fastest=1,
    )

    print("--")

# ---------------------------------------------------------------