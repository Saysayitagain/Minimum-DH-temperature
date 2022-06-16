import pandas as pd

from ReadData import readcap
from HeatingCapacity import HeatingCap
from EnergyConsumption import energycal
from HCAcalculation import HCAcal
from UniformTemperatureCaculation import Unical
from CriticalTemperatureCalculation import Crical


Buildinglist = [5]
for i in Buildinglist:
    [df1, df2, egy_data, WeeklyHCA, Heat_Area, Wkl_HDD, Pipe_Heatloss] = readcap(i)

    [Total_Cap, Apart_Cap, Reg_Cap] = HeatingCap(df1, df2, i)
    [Wkl_SH_Egy, Four_day_SH_Egy_Uni] = energycal(egy_data)

    [Avg_Area, Mass_flw_rate, Inp_Cap, Avg_Hlc, Heat_Area_Uni, Mass_flw_rate_Uni, Inp_Cap_Uni, SH_HG_Egy_Uni,
     Wkl_HDD] = HCAcal(WeeklyHCA, Heat_Area, Wkl_HDD, Wkl_SH_Egy, Four_day_SH_Egy_Uni, Apart_Cap, Total_Cap, Pipe_Heatloss, i)
    #print(Reg_Cap[1])
    #print(i)
    print(Heat_Area_Uni.sum())
    print(Mass_flw_rate_Uni)
    print(Inp_Cap_Uni)
    print(SH_HG_Egy_Uni)


    [Sup_uni, Ret_uni] = Unical(Heat_Area_Uni, Mass_flw_rate_Uni, Inp_Cap_Uni, SH_HG_Egy_Uni, Wkl_HDD)

    [Sup_cri, Ret_cri]\
        = Crical(Avg_Area, Mass_flw_rate, Inp_Cap, Avg_Hlc)
    #print(Sup_cri)
    #print(Sup_uni)
    writer = pd.ExcelWriter('Out{number}.xlsx'.format(number=i))
    Sup_cri.to_excel(writer, sheet_name='Sup cri')
    Ret_cri.to_excel(writer, sheet_name='Ret cri')
    Sup_uni.to_excel(writer, sheet_name='Sup uni')
    Ret_uni.to_excel(writer, sheet_name='Ret uni')
    writer.save()
    writer.close()







