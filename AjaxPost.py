import os
import FindMode
import NeuralNet
import pandas as pd
import pickle
from flask import Flask,render_template, request,json
import KNNModel

app = Flask(__name__)

@app.route('/predictIncident', methods=['POST'])
def predictIncident():
#     dayOfWeek =  request.form['dayOfWeek']
#     time = request.form['time']
#     lat = request.form['lat']
#     long = request.form['long']

    dayOfWeek = "Sunday"
    time = 000
    radius = 20
    lat = [35, 22, -15, 7]
    long = [-80, 9, 29, 17]
    
    dicDayValues = {'Sunday':'0','Monday':'1','Tuesday':'2','Wednesday':'3',
                    'Thursday':'4','Friday':'5','Saturday':'6'}
    
#     day = dicDayValues.get(dayOfWeek)
    day = dayOfWeek
    #Calculate mode Primary Cause and Crash Type for comparison to our model's return data
    #We need to remove radius and replace it with a list latitude, longitude values
    modePrimaryCause = FindMode.findMode(day, lat[0], long[0], radius)
    modeCrashType = FindMode.findMode(day, lat[0], long[0], radius)
    print("modePrimaryCause ", modePrimaryCause)
    print("modeCrashType ", modeCrashType)
        
   
    

    primaryCauseResult = KNNModel.predict(time, lat[0], long[0])
    crashType = KNNModel.predict(time, lat[0], long[0])
#         pCDataFrame.append(KNNModel.predict(time, lat[i], long[i]))
#         cTDataFrame.append(KNNModel.predict(time, lat[i], long[i]))


#     pCDataFrame.append(KNNModel.predict(time, latitude[i], longitude[i]))
#     cTDataFrame.append(KNNModel.predict(time, latitude[i], longitude[i]))
        
    dicPrimaryCause, dicCrashType = loadDictionaries()
    
    predictedPrimaryCause = dicPrimaryCause[primaryCauseResult[0]]
    predictedCrashType = dicCrashType[crashType[0]]
    
    print("Done")
    return json.dumps({'status':'OK','modePrimaryCause':modePrimaryCause,'modeCrashType':modeCrashType,
                       'predictedPrimaryCause':predictedPrimaryCause,'predictedCrashType':predictedCrashType})
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
    #app.run()
    predictIncident();
    