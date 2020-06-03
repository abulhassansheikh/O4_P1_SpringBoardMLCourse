# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:22:20 2020

@author: AHS
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello, world!"

if __name__=="__main__":
    app.run(debug=True)
