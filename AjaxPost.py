import os
import FindMode
import NeuralNet
import pandas as pd
import pickle
from flask import Flask,render_template, request,json

app = Flask(__name__)

@app.route('/predictIncident', methods=['POST'])
def predictIncident():
    dayOfWeek =  request.form['dayOfWeek']
    time = request.form['time']
    lat = request.form['lat']
    long = request.form['long']
    
    dicDayValues = {'Sunday':'0','Monday':'1', 'Tuesday':'2','Wednesday':'3',
                    'Thursday':'4','Friday':'5','Saturday':'6'}
    
    day = dicDayValues.get(dayOfWeek)
    #Calculate mode Primary Cause and Crash Type for comparison to our model's return data
    #We need to remove radius and replace it with a list latitude, longitude values
    modePrimaryCause = FindMode.findMode(day, time, radius, latitude, longitude)
    modeCrashType = FindMode.findMode(day, time, radius, latitude, longitude)
        
#     pCDataFrame = pd.DataFrame()
#     cTDataFrame = pd.DataFrame
#     for i in len(lat):
#         pCDataFrame.append(NeuralNet.predictValue(day, time, latitude[i], longitude[i]))
#         cTDataFrame.append(NeuralNet.predictValue(day, time, latitude[i], longitude[i]))
#         
#     predictedPrimaryCauseVal = pCDataFrame.mode()
#     predictedCrashTypeVal = cTDataFrame.mode()
#     
#     dicPrimaryCause, dicCrashType = loadDictionaries()
#     
#     predictedPrimaryCause = dicPrimaryCause.get(predictedPrimaryCauseVal)
#     predictedCrashType = dicCrashType.get(predictedCrashTypeVal)
    
    
    return json.dumps({'status':'OK','modePrimaryCause':modePrimaryCause,'modeCrashType':modeCrashType,
                       'predictedPrimaryCause':"primaryCause",'predictedCrashType':"predictedCrashType"})
    #return json.dumps({'status':'OK','user':user,'pass':password})

def loadDictionaries():
    open_dicPrimaryCause = open("dicPrimaryCause.pickle", "rb")
    dicPrimaryCause = pickle.load(open_dicPrimaryCause)
    open_dicPrimaryCause.close()
  
    open_dicCrashType = open("dicCrashType.pickle", "rb")
    dicCrashType = pickle.load(open_dicCrashType)
    open_dicCrashType.close()
    
    return dicPrimaryCause, dicCrashType

if __name__=="__main__":
    app.run()