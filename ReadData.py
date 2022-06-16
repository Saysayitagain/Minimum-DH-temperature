import pandas as pd



def readcap(n):
    '''Read the Registered capacity and 2-month HCA for every radiator'''
    df1 = pd.read_excel("raw data/InputsForAfd{number}.xlsx".format(number=n), 'RegisteredCapacity')

    df2 = pd.read_excel("raw data/InputsForAfd{number}.xlsx".format(number=n), 'Radiator2monthHCA')

    egy_comp = pd.read_excel("raw data/InputsForAfd{number}.xlsx".format(number=n), 'EnergyConsumption')

    WeeklyHCA = pd.read_excel("raw data/InputsForAfd{number}.xlsx".format(number=n), 'FlatWeeklyHCA')

    Heat_Area = pd.read_excel("raw data/InputsForAfd{number}.xlsx".format(number=n), 'ApartmentArea')

    Wkl_HDD = pd.read_excel("raw data/InputsForAfd{number}.xlsx".format(number=n), 'WeeklyHDD')

    Pipe_Heatloss = pd.read_excel("raw data/InputsForAfd{number}.xlsx".format(number=n), 'Pipe')

    return df1, df2, egy_comp, WeeklyHCA, Heat_Area, Wkl_HDD, Pipe_Heatloss


