import pandas as pd
import numpy as np


def HCAcal(WeeklyHCA, Heat_Area, Wkl_HDD, Wkl_SH_Egy, Four_day_SH_Egy_Uni, Apart_Cap, Total_Cap, Pipe_Heatloss, i):

    WeeklyHCAShare = pd.DataFrame(
        columns=['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8', 'Week 9'])
    for wi in range(1, WeeklyHCA.shape[1]):
        WeeklyHCAShare['Week {week}'.format(week=wi)] = WeeklyHCA['Week {week}'.format(week=wi)] / WeeklyHCA[
            'Week {week}'.format(week=wi)].sum()

    #print('HCA share', WeeklyHCAShare)

    Heat_Area_Uni = Heat_Area.sum()

    SH_Egy = pd.DataFrame(
        columns=['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8', 'Week 9'])
    for fi in range(0, WeeklyHCAShare.shape[0]):
        SH_Egy = pd.concat([SH_Egy, WeeklyHCAShare.iloc[fi] * Wkl_SH_Egy])



    SH_Egy.reset_index(inplace=True)
    if i == 2 or i == 4 or i == 5:
        SH_Egy.drop([len(SH_Egy) - 1], inplace=True)


    SH_HG_Egy = pd.DataFrame(
        columns=['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8', 'Week 9'])
    for wi in range(1, WeeklyHCA.shape[1]):
        SH_HG_Egy['Week {week}'.format(week=wi)] = SH_Egy['Week {week}'.format(week=wi)] * 1000 + 5 * 7 * 24 / 1000 * \
                                                   Heat_Area['Area']
    SH_HG_Egy = SH_HG_Egy.astype('float64')

    SH_HG_Egy_Uni = SH_HG_Egy.sum().sum() / 1000

    Hlc = pd.DataFrame(
        columns=['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8', 'Week 9'])
    for fi in range(0, SH_HG_Egy.shape[0]):
        Hlc = pd.concat([Hlc, SH_HG_Egy.iloc[fi] / Wkl_HDD / 24])


    Hlc.reset_index(inplace=True)
    Hlc = Hlc.drop(['index'], axis=1)


    Hlc_by_Cap = pd.DataFrame(
        columns=['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8', 'Week 9'])
    for wi in range(1, 10):
        Hlc_by_Cap['Week {week}'.format(week=wi)] = Hlc['Week {week}'.format(week=wi)] / (
                Apart_Cap['Larger of active and 75(W)'] / 1000)

    Hlc_by_Cap = Hlc_by_Cap.astype('float64')
    #print('Hlc by capacity',Hlc_by_Cap)
    Cri_Pos = Hlc_by_Cap.idxmax()
    print('Critical position',Cri_Pos)

    Cri_Area = pd.DataFrame()
    for fi in range(1, 10):
        Cri_Area = pd.concat([Cri_Area, Heat_Area.iloc[Cri_Pos['Week {week}'.format(week=fi)]]])
    Cri_Area.reset_index(inplace=True)
    Cri_Area.columns = ['Name', 'Area (m2)']
    Avg_Area = Cri_Area['Area (m2)'].mean()

    Cri_Cap = pd.DataFrame()
    for fi in range(1, 10):
        Cri_Cap = pd.concat([Cri_Cap, Apart_Cap.iloc[Cri_Pos['Week {week}'.format(week=fi)]]])
    Cri_Cap.reset_index(inplace=True)
    Cri_Cap = Cri_Cap.loc[Cri_Cap['index'] == 'Larger of active and 75(W)']
    Cri_Cap.columns = ['Name', 'Capacity(W)']
    Avg_Cap = Cri_Cap['Capacity(W)'].mean()
    Avg_Cap = Avg_Cap / 1000
    Corr_fac = 1 + Pipe_Heatloss.columns[0] / Apart_Cap['Registered Capacity(W)'].sum() * 1000
    #print(Apart_Cap['Larger of active and 75(W)'].sum())

    Inp_Cap = Corr_fac * Avg_Cap
    Inp_Cap_Uni = Corr_fac * Total_Cap
    #print(Cri_Pos['Week {week}'.format(week=9)])


    Cri_Hlc = pd.Series(np.arange(9))
    for fi in range(1, 10):
        Cri_Hlc[fi-1] = Hlc.loc[
            [Cri_Pos['Week {week}'.format(week=fi)]], ['Week {week}'.format(week=fi)]].values


    Avg_Hlc = Cri_Hlc.mean()[0][0]

    Cri_Egy = pd.Series(np.arange(9))
    for fi in range(1, 10):
        Cri_Egy[fi-1] = SH_HG_Egy.loc[
            [Cri_Pos['Week {week}'.format(week=fi)]], ['Week {week}'.format(week=fi)]].values



    Avg_Egy = Cri_Egy.mean()

    Mass_flw_rate = Avg_Egy / (7 * 24 * 4.2 * 10)
    Mass_flw_rate_Uni = Four_day_SH_Egy_Uni / (4 * 24 * 4.2 * 10) * 1000

    return Avg_Area, Mass_flw_rate, Inp_Cap, Avg_Hlc, Heat_Area_Uni, Mass_flw_rate_Uni, Inp_Cap_Uni, SH_HG_Egy_Uni, Wkl_HDD


