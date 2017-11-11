import pandas as pd

df = pd.read_csv('traffic.csv')
df.fillna(0, inplace=True)

def createDictionary():
    dicPrimaryCause = {}
    dicCrashType = {}
    dicDayValues = {'0':'Sunday','1':'Monday', '2':'Tuesday','3':'Wednesday',
                    '4':'Thursday','5':'Friday','6':'Saturday'}
    
    
    
    for index, row in df.iterrows():
        dicPrimaryCause[int(row['PRIMARY_CAUSE_CD'])]= row['PRIMARY_CAUSE']
        dicCrashType[int(row['CRSH_TYPE_CD'])]= row['CRASH_TYPE']
    return dicPrimaryCause, dicCrashType, dicDayValues


def getData():
    return df

