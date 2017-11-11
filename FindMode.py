import math
import numpy

def findMode(dow, lat, log, radius, data):
    df_filtered = data[((data['LATITUDE'] >= lat-radius) & (data['LATITUDE'] <= lat+radius))]
    df_filtered = df_filtered[((df_filtered['LONGITUDE'] >= log-radius) & (df_filtered['LONGITUDE'] <= log+radius))]
    df_filtered = df_filtered[(df_filtered['DAY_OF_WEEK_DESC'] == dow)]
    #df_filtered = df_filtered[(df_filtered['PRIMARY_CAUSE_CD'] > 0)]
    #df_filtered = df_filtered[(df_filtered['CRSH_TYPE_CD'] > 0)]
    modePrimaryCause = df_filtered['PRIMARY_CAUSE_CD'].mode()
    modeCrashType = df_filtered['CRSH_TYPE_CD'].mode()
    return modePrimaryCause[0], modeCrashType[0]

