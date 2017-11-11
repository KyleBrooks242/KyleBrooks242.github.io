import math
import numpy
import pickle
import ReadAndCreateDic as reader

def findMode(dow, lat, log, radius):
    data = reader.getData()
    open_dicPrimaryCause = open("dicPrimaryCause.pickle", "rb")
    dicPrimaryCause = pickle.load(open_dicPrimaryCause)
    open_dicPrimaryCause.close()
  
    open_dicCrashType = open("dicCrashType.pickle", "rb")
    dicCrashType = pickle.load(open_dicCrashType)
    open_dicCrashType.close()
            
    df_filtered = data[((data['LATITUDE'] >= lat-radius) & (data['LATITUDE'] <= lat+radius))]
    df_filtered = df_filtered[((df_filtered['LONGITUDE'] >= log-radius) & (df_filtered['LONGITUDE'] <= log+radius))]
    df_filtered = df_filtered[(df_filtered['DAY_OF_WEEK_DESC'] == dow)]
    #df_filtered = df_filtered[(df_filtered['PRIMARY_CAUSE_CD'] > 0)]
    #df_filtered = df_filtered[(df_filtered['CRSH_TYPE_CD'] > 0)]
    modePrimaryCauseVal = df_filtered['PRIMARY_CAUSE_CD'].mode()
    modeCrashTypeVal = df_filtered['CRSH_TYPE_CD'].mode()
    
    modePrimaryCause = dicPrimaryCause.get(round(modePrimaryCauseVal[0]))
    modeCrashType = dicCrashType.get(round(modeCrashTypeVal[0]))
    
    if (modePrimaryCause == None):
        modePrimaryCause = "Predicted Primary Cause was out of defined range."
    if (modeCrashType == None):
        modeCrashType = "Predicted Crash Type was out of defined range."
    
    return modePrimaryCause, modeCrashType

