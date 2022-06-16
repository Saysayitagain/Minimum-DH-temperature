import pandas as pd
import matplotlib.pyplot as plt


def HeatingCap(df1, df2, i):
    Reg_Cap = df1.groupby(['Location No']).sum()
    Reg_Cap = Reg_Cap['Performance (W)']*0.75
    inner_join = pd.merge(df1, df2, on='Meter No', how='inner')
    Rad_Cap = inner_join.loc[:, ['Building No', 'Location No', 'Meter No', 'Performance (W)', 'Consumption']]
    Rad_Cap['InUse'] = Rad_Cap['Consumption'] > 10

    Rad_Cap['Registered Capacity(W)'] = Rad_Cap['Performance (W)']
    Rad_Cap['Active Capacity(W)'] = Rad_Cap['InUse'] * Rad_Cap['Performance (W)']
    Apart_Cap = Rad_Cap.groupby(['Location No']).sum()

    Apart_Cap = Apart_Cap.drop(columns=['Building No', 'Meter No', 'Performance (W)', 'Consumption', 'InUse'])
    Apart_Cap['Original 75 Capacity(W)'] = Reg_Cap

    Apart_Cap['75 Registered Capacity(W)'] = 0.75 * Apart_Cap['Registered Capacity(W)']
    Apart_Cap['Larger of active and 75(W)'] = Apart_Cap[['Active Capacity(W)','Original 75 Capacity(W)']].max(axis=1)
    Apart_Cap.reset_index(inplace=True)
    if i == 2 or i == 4 or i == 5:
        Apart_Cap.drop([len(Apart_Cap) - 1], inplace=True)


    Total_Cap = Apart_Cap['Larger of active and 75(W)'].sum()
    print( Apart_Cap['Larger of active and 75(W)'])


    return Total_Cap, Apart_Cap, Reg_Cap


