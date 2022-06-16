import math

import pandas as pd
from sympy import *


def Crical(Avg_Area, Mass_flw_rate, Inp_Cap, Avg_Hlc):
    Floor_Area = Avg_Area
    Flow_rate = Mass_flw_rate
    Heat_Cap = Inp_Cap
    Hlc = Avg_Hlc
    Sup_Dsn = 90
    Ret_Dsn = 70
    Ind_tep = 20
    Heat_gain = 5
    LMTD_0 = (Sup_Dsn - Ret_Dsn) / math.log((Sup_Dsn - Ind_tep) / (Ret_Dsn - Ind_tep))

    Out_Temp = pd.Series(range(-12, 13))
    HDD = 22 - Out_Temp
    Heat_load = Hlc * HDD - Heat_gain * Floor_Area / 1000
    Rela_Heat_load = Heat_load / Heat_Cap
    LMTD_required = Rela_Heat_load ** (1 / 1.3) * LMTD_0

    Sup_Cri = pd.Series(range(-12, 13))
    Ret_Cri = pd.Series(range(-12, 13))
    s = Symbol('s')
    r = Symbol('r')
    for i in range(0, 25):
        expr2 = [4.2 * Flow_rate * (s - r) - Heat_load[i],
                 (s - r) / log((s - Ind_tep) / (r - Ind_tep)) - LMTD_required[i]]
        r2 = solve(expr2, [s, r])
        Sup_Cri[i] = r2[0][0]
        Ret_Cri[i] = r2[0][1]

    return Sup_Cri, Ret_Cri





