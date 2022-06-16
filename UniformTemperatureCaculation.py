import math

import pandas as pd
from sympy import *


def Unical(Heat_Area_Uni, Mass_flw_rate_Uni, Inp_Cap_Uni, SH_HG_Egy_Uni, Wkl_HDD):
    Floor_Area = Heat_Area_Uni.sum()
    Flow_rate = Mass_flw_rate_Uni
    Flow_rate = 1.54
    Heat_Cap = Inp_Cap_Uni
    SH_HG_Egy = SH_HG_Egy_Uni
    Total_HDD = Wkl_HDD.sum().sum()
    Hlc = SH_HG_Egy * 1000 / (Total_HDD * 24)

    Sup_Dsn = 90
    Ret_Dsn = 70
    Ind_tep = 20
    Heat_gain = 5
    LMTD_0 = (Sup_Dsn - Ret_Dsn) / math.log((Sup_Dsn - Ind_tep) / (Ret_Dsn - Ind_tep))

    Out_Temp = pd.Series(range(-12, 13))
    HDD = 22 - Out_Temp
    Heat_load = Hlc * HDD - Heat_gain * Floor_Area / 1000

    Rela_Heat_load = Heat_load / Heat_Cap * 1000

    LMTD_required = Rela_Heat_load ** (1 / 1.3) * LMTD_0

    Sup_Uni = pd.Series(range(-12, 13))
    Ret_Uni = pd.Series(range(-12, 13))
    s = Symbol('s')
    r = Symbol('r')
    for i in range(0, 25):
        expr2 = [4.2 * Flow_rate * (s - r) - Heat_load[i],
                 (s - r) / log((s - Ind_tep) / (r - Ind_tep)) - LMTD_required[i]]
        r2 = solve(expr2, [s, r])
        Sup_Uni[i] = r2[0][0]
        Ret_Uni[i] = r2[0][1]

    return Sup_Uni, Ret_Uni

