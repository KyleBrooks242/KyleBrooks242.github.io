import pandas as pd

df = pd.read_csv('traffic.csv')
df.fillna(0, inplace=True)

def createDictionary():
    dicPrimaryCause = {}
    dicCrashType = {}
    dicDayValues = {'Sunday':'0','Monday':'1', 'Tuesday':'2','Wednesday':'3',
                    'Thursday':'4','Friday':'5','Saturday':'6'}
      
    for index, row in df.iterrows():
        dicPrimaryCause[int(row['PRIMARY_CAUSE_CD'])]= row['PRIMARY_CAUSE']
        dicCrashType[int(row['CRSH_TYPE_CD'])]= row['CRASH_TYPE']
    return dicPrimaryCause, dicCrashType, dicDayValues


def getData():
    return df

