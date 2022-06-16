import pandas as pd

pd.set_option('display.max_columns', None)

def energycal(Egy_Comp):
    E1 = Egy_Comp.loc[Egy_Comp['Date'] == '2021-05-31', 'Energy'].values
    E2 = Egy_Comp.loc[Egy_Comp['Date'] == '2021-07-31', 'Energy'].values
    E3 = E2 - E1
    Wkl_DHW_Egy = E3 / 61 * 7
    #print(Wkl_DHW_Egy)

    Wkl_SH_Egy = {'Week 1': [Egy_Comp.loc[Egy_Comp['Date'] == '2021-12-07', 'Energy'].values - Egy_Comp.loc[
        Egy_Comp['Date'] == '2021-11-30', 'Energy'].values],
                  'Week 2': [Egy_Comp.loc[Egy_Comp['Date'] == '2021-12-14', 'Energy'].values - Egy_Comp.loc[
                      Egy_Comp['Date'] == '2021-12-07', 'Energy'].values],
                  'Week 3': [Egy_Comp.loc[Egy_Comp['Date'] == '2021-12-21', 'Energy'].values - Egy_Comp.loc[
                      Egy_Comp['Date'] == '2021-12-14', 'Energy'].values],
                  'Week 4': [Egy_Comp.loc[Egy_Comp['Date'] == '2021-12-27', 'Energy'].values - Egy_Comp.loc[
                      Egy_Comp['Date'] == '2021-12-21', 'Energy'].values + 0.5*(Egy_Comp.loc[Egy_Comp['Date'] == '2021-12-29', 'Energy'].values-Egy_Comp.loc[Egy_Comp['Date'] == '2021-12-27', 'Energy'].values)],
                  'Week 5': [Egy_Comp.loc[Egy_Comp['Date'] == '2022-01-04', 'Energy'].values - Egy_Comp.loc[
                      Egy_Comp['Date'] == '2021-12-29', 'Energy'].values + 0.5*(Egy_Comp.loc[Egy_Comp['Date'] == '2021-12-29', 'Energy'].values-Egy_Comp.loc[Egy_Comp['Date'] == '2021-12-27', 'Energy'].values)],
                  'Week 6': [Egy_Comp.loc[Egy_Comp['Date'] == '2022-01-11', 'Energy'].values - Egy_Comp.loc[
                      Egy_Comp['Date'] == '2022-01-04', 'Energy'].values],
                  'Week 7': [Egy_Comp.loc[Egy_Comp['Date'] == '2022-01-18', 'Energy'].values - Egy_Comp.loc[
                      Egy_Comp['Date'] == '2022-01-11', 'Energy'].values],
                  'Week 8': [Egy_Comp.loc[Egy_Comp['Date'] == '2022-01-25', 'Energy'].values - Egy_Comp.loc[
                      Egy_Comp['Date'] == '2022-01-18', 'Energy'].values],
                  'Week 9': [Egy_Comp.loc[Egy_Comp['Date'] == '2022-02-01', 'Energy'].values - Egy_Comp.loc[
                      Egy_Comp['Date'] == '2022-01-25', 'Energy'].values]
                  }

    Wkl_SH_Egy = pd.DataFrame(Wkl_SH_Egy) - float(Wkl_DHW_Egy)

    Four_day_Egy_Uni = [Egy_Comp.loc[Egy_Comp['Date'] == '2022-01-26', 'Energy'].values - Egy_Comp.loc[
        Egy_Comp['Date'] == '2022-01-22', 'Energy'].values]
    Four_day_SH_Egy_Uni = Four_day_Egy_Uni - Wkl_DHW_Egy * 4 / 7
    Four_day_SH_Egy_Uni = Four_day_SH_Egy_Uni[0][0]

    if Egy_Comp.at[10, 'Unit'] == 'kWh':
        Wkl_SH_Egy = Wkl_SH_Egy / 1000
        Four_day_SH_Egy_Uni = Four_day_SH_Egy_Uni / 1000


    return Wkl_SH_Egy, Four_day_SH_Egy_Uni





