import pickle
import json
import config
import numpy as np
# creating class for user input 

class Diabeties():
    def __init__(self,Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
        self.Pregnancies=Pregnancies
        self.Glucose=Glucose
        self.BloodPressure=BloodPressure
        self.SkinThickness=SkinThickness
        self.Insulin=Insulin
        self.BMI=BMI
        self.DiabetesPedigreeFunction=DiabetesPedigreeFunction
        self.Age=Age


    def load_model(self):
        with open(diabetes_model_path,'rb') as  file:
            self.model=pickle.load(file)

        with open(diabetes_json_path,'r') as file:
            self.json_data=json.load(file)




    def get_predict_diabetes(self):
        self.load_model()
        # pass value to test array
        test_array=np.zeros(len(self.json_data['columns']))
        test_array[0]=self.Pregnancies
        test_array[1]=self.Glucose
        test_array[2]=self.BloodPressure
        test_array[3]=self.SkinThickness
        test_array[4]=self.Insulin
        test_array[5]=self.BMI
        test_array[6]=self.DiabetesPedigreeFunction
        test_array[7]=self.Age
        result=self.model.predict([test_array])
        return result