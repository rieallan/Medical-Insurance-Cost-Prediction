import pandas as pd
import pickle



with open('Insurance_Prediction.ipynb', 'rb') as f:
    data = f.read()


with open('Insurance_Prediction.pkl', 'wb') as f:
    pickle.dump(data, f)



class Predictions():

    def __init__(self,age,sex,bmi,child,smoke,reg):

        self.age= age
        self.sex = sex
        self.bmi = bmi
        self.child = child
        self.smoke = smoke
        self.reg = reg

    def predict(self):

        pkl_in = open("Insurance_Prediction.pkl",'rb')
        reg = pickle.load(pkl_in)
        prediction = reg.predict(pd.DataFrame(data={'age':[self.age],'sex':[self.sex],'bmi':[self.bmi],'children':[self.child],'smoker':[self.smoke],'region':[self.reg]})) 
        
        return(str(prediction[0].round(2)))



class PredictionFile():

    def __init__(self,csvfile):

        self.csvfile = csvfile

    def predictfile(self):

        df = pd.read_csv(self.csvfile, encoding='cp1252')
        pkl_in = open("Insurance_Prediction.pkl",'rb')
        reg = pickle.load(pkl_in)
        pred = reg.predict(df)
        pred = pd.Series(pred,name='Predicted Insurance cost')
        newdf = pd.concat([df,pred],axis=1)

        return(newdf)