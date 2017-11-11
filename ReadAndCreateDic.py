import pandas as pd

df = pd.read_csv('traffic.csv')
df.fillna(0, inplace=True)

def createDictionary():
    dicPrimaryCause = {}
    dicCrashType = {}
    for index, row in df.iterrows():
        dicPrimaryCause[int(row['PRIMARY_CAUSE_CD'])]= row['PRIMARY_CAUSE']
        dicCrashType[int(row['CRSH_TYPE_CD'])]= row['CRASH_TYPE']
    return dicPrimaryCause, dicCrashType


def getData():
    return df

