# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 08:06:57 2020

@author: AHS
"""

# Create model prediction function
def PTweightPred(PTdimPre):
    #Import packages
    import pandas as pd
    import numpy as np
    import os

    Dim_model = (pd.read_csv(r"Dim_model.csv",encoding='utf-8'))    
    
    intercept = Dim_model.coef[0]
    heightCoef = Dim_model.coef[1]
    lenghtCoef = Dim_model.coef[2]
    widthCoef = Dim_model.coef[3]
    volumeCoef = Dim_model.coef[4]
    
    uHeight, bHeight = PTdimPre[0, 0:2]
    uLength, bLength = PTdimPre[0, 2:4]
    uWidth, bWidth = PTdimPre[0, 4:6]
    uVolume = uHeight * uLength * uWidth
    bVolume = bHeight * bLength * bWidth

    uWeight = (intercept + heightCoef*uHeight + lenghtCoef*uLength + 
                          widthCoef*uWidth + volumeCoef*uVolume) 
    bWeight = (intercept + heightCoef*bHeight + lenghtCoef*bLength + 
                          widthCoef*bWidth + volumeCoef*bVolume)
    
    return (np.array([uWeight, bWeight]))

# Create model prediction function
def PTdefPred(pt):
    #Import packages
    import pandas as pd
    import numpy as np
    import os

    PTRef = (pd.read_csv(r"Pt2LWH_model.csv",encoding='utf-8'))
    
    dim = (PTRef[PTRef["part_type"]==pt][['height_max', 'height_min',
                                         'length_max', 'length_min',
                                         'width_max', 'width_min']])
    return (np.array(dim))
     



