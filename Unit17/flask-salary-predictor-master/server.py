# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Load the model
os.chdir("C:/Users/abulh/Sync/O4_P1_SpringBoardMLCourse/Unit17/flask-salary-predictor-master")
from I2Dmodel import *

#,methods=['POST']
@app.route('/api/<string:PT>')
def predict(PT):
    # Get the data from the POST request.
    #data = request.get_json(force=True)

    PT = PT.replace("+", " ")
    LWHprediction = PTdefPred(PT)

    Weightprediction = PTweightPred(LWHprediction)

    
    #Make prediction Dict
    output = {
            #"Part Type": data['exp'],
            "Part Type": PT,
            "Max Length": LWHprediction[0][0],
            "Min Length": LWHprediction[0][1],
            "Max Width": LWHprediction[0][2],
            "Min Width": LWHprediction[0][3],
            "Max Height": LWHprediction[0][4],
            "Min Height": LWHprediction[0][5],
            "MaxWeight": Weightprediction[0],
            "MinWeight": Weightprediction[1],
            }


    return jsonify(output)

@app.route('/test/<string:PT>')
def test(PT):
    #arg1 = request.args["arg1"]
    PT = PT.replace("+", " ")
    return PT


if __name__ == '__main__':
        app.run(port=5000, debug=True)


