from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server
import pickle
import numpy as np


model = pickle.load(open('regression_rf.pkl', 'rb'))

app = Flask(__name__)


def predict():
    
    put_text('Welcome to the Machine Learning Stroke Likehood Predictor')
    
    gender = select("Enter your gender: ", ['Male', 'Female'])
    if (gender == 'Male'):
        gender = 1407
    else:
        gender = 2159
    
    age = input("Enter your age: ", type=NUMBER)
    
    hypertension = select("Have you had hypertension: ", ['Yes', 'No'])
    if (hypertension == 'Yes'):
        hypertension = 446
    else: 
        hypertension = 3120
    
    heart_disease = select("Have you had heart disease: ", ['Yes', 'No'])
    if (heart_disease == 'Yes'):
        heart_disease = 228
    else: 
        heart_disease = 3337
        
    work_type = select("What kind of work do you do: ", ['Private', 'Self-Employed', 'Govt_job', 'Children', 'Never_worked'])
    if (work_type == 'Private'):
        work_type = 2284
    elif (work_type == 'Self-Employed'): 
        work_type = 663
    elif (work_type == 'Govt_job'): 
        work_type = 535
    elif (work_type == 'Children'): 
        work_type = 69
    else:
        work_type = 14
        
    ever_married = select("Have you ever been married: ", ['Yes', 'No'])
    if (ever_married == 'Yes'):
        ever_married = 2710
    else: 
        ever_married = 855
        
    Residence_type = select("What is your residence type: ", ['Urban', 'Rural'])
    if (Residence_type == 'Urban'):
        Residence_type = 1814
    else: 
        Residence_type = 1751
    
    avg_glucose_level = input("Enter your average glucose level: ", type=FLOAT)
    
    bmi = input("Enter your bmi: ", type=FLOAT)
    
    smoking_status = select("What is your smoking status: ", ['Never Smoked', 'Formerly Smoked', 'Smokes'])
    if (smoking_status == 'Never Smoked'):
        smoking_status = 1892
    elif (smoking_status == 'Formerly Smoked'): 
        smoking_status = 884
    else: 
        smoking_status = 789
    
    prediction = model.predict([[gender, age, hypertension, heart_disease, ever_married, avg_glucose_level, bmi]])
    output = round(prediction[0], 2)

    put_text(prediction)
    
    if output == 1:
        put_text("You have been predicted to have a future stroke.")

    else:
        put_text('You are not predicted to have a future stroke.')

#app.add_url_rule('/tool', 'webio_view', webio_view(predict),
 #           methods=['GET', 'POST', 'OPTIONS'])


#if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument("-p", "--port", type=int, default=8080)
    #args = parser.parse_args()

    #start_server(predict, port=args.port)
#if __name__ == '__main__':
    #predict()

#app.run(host='localhost', port=80)
