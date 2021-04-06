# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 11:41:36 2021

@author: Admin
"""

import os
os.getcwd()
os.chdir('D:\machine learning\Bank note authentication')


from flask import Flask,request
import pandas as pd
import numpy as np
import pickle



app=Flask(__name__)
pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)


@app.route('/')
def welcome():
    return"Welcome ALL"

@app.route('/predict')
def predict_note_authentication():
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is" + str(prediction)

if __name__=='__main__':
    app.run()
   