# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 14:50:52 2020

@author: AHS
"""
from flask import Flask
import os
import pandas as pd

application = Flask(__name__)

@application.route('/')
def hello_world():
    np = '/opt/python/current/app'
    os.chdir(np)
    PTRef = (pd.read_csv(r"Pt2LWH_model.csv",encoding='utf-8'))
    return str(PTRef)

@application.route('/test/<string:test>')
def testFun(test):
    return test

if __name__ == '__main__':
    application.run(debug=True)
    
#/opt/python/current/app
#/opt/python/bundle/40/app
#np = "C:/Users/abulh/Sync/O4_P1_SpringBoardMLCourse/Unit17/TestDeployment"



    
    



