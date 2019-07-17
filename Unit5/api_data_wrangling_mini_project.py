#!/usr/bin/env python
# coding: utf-8

# This exercise will require you to pull some data from the Qunadl API. 
#Qaundl is currently the most widely used aggregator of financial market data.

# As a first step, you will need to register a free account on the 
#http://www.quandl.com website.

# After you register, you will be provided with a unique API key, 
#that you should store:

# In[ ]:


# Store the API key as a string - according to PEP8, constants are always 
#named in all upper case
API_KEY = 'xS1u4awxhU3Pc6anb9WL'


# Qaundl has a large number of data sources, but, unfortunately, most of them 
#require a Premium subscription. Still, there are also a good number of free datasets.

# For this mini project, we will focus on equities data from the Frankfurt 
#Stock Exhange (FSE), which is available for free. We'll try and analyze the 
#stock prices of a company called Carl Zeiss Meditec, which manufactures tools 
#for eye examinations, as well as medical lasers for laser eye surgery: 
#https://www.zeiss.com/meditec/int/home.html. The company is listed under 
#the stock ticker AFX_X.

# You can find the detailed Quandl API instructions here: 
#https://docs.quandl.com/docs/time-series

# While there is a dedicated Python package for connecting to the Quandl API, 
#we would prefer that you use the *requests* package, which can be easily 
#downloaded using *pip* or *conda*. You can find the documentation for the 
#package here: http://docs.python-requests.org/en/master/ 

# Finally, apart from the *requests* package, you are encouraged to not use any 
#third party Python packages, such as *pandas*, and instead focus on what's 
#available in the Python Standard Library (the *collections* module might come in 
#handy: https://pymotw.com/3/collections/).
# Also, since you won't have access to DataFrames, you are encouraged to us 
#Python's native data structures - preferably dictionaries, though some 
#questions can also be answered using lists.
# You can read more on these data structures here: 
#https://docs.python.org/3/tutorial/datastructures.html

# Keep in mind that the JSON responses you will be getting from the API 
#map almost one-to-one to Python's dictionaries. Unfortunately, they can be 
#very nested, so make sure you read up on indexing dictionaries in the 
#documentation provided above.

#----

# First, import the relevant modules

import requests
import collections 
import json
#----

# Now, call the Quandl API and pull out a small sample of the data 
#(only one day) to get a glimpse
# into the JSON structure that will be returned

data = {"database_code":"FSE", 
        "dataset_code":"AFX_X"}

FSE/AFX_X.json?api_key=xS1u4awxhU3Pc6anb9WL

url = "https://www.quandl.com/api/v3/datasets/FSE/AFX_X.json?start_date=2019-07-01&end_date=2019-07-01&api_key=xS1u4awxhU3Pc6anb9WL"
test = requests.get(url)
test.status_code
jsonData = json.loads(test.text)
#----

# Inspect the JSON structure of the object you created, and take note of how 
#nested it is,
# as well as the overall structure


# These are your tasks for this mini project:
# 
# 1. Collect data from the Franfurt Stock Exchange, for the ticker AFX_X, for 
#the whole year 2017 (keep in mind that the date format is YYYY-MM-DD).
url = "https://www.quandl.com/api/v3/datasets/FSE/AFX_X.json?start_date=2017-01-01&end_date=2017-12-31&api_key=xS1u4awxhU3Pc6anb9WL"
Extract = requests.get(url)
Extract.status_code

# 2. Convert the returned JSON object into a Python dictionary.
jsonData = json.loads(Extract.text)
head(jsonData)
print(type(jsonData))

# 3. Calculate what the highest and lowest opening prices were for the stock in 
#this period.

AllOpeningPrices = [50]

for d in range(0,254):
    OpeningPrice = jsonData["dataset"]["data"][d][1]
    
    if OpeningPrice != None:
        AllOpeningPrices.append(OpeningPrice)

max(AllOpeningPrices) #53.11
min(AllOpeningPrices) #34.0

    
# 4. What was the largest change in any one day (based on High and Low price)?
AllPriceDiff = [0, 0]

for d in range(0,254):
    HighPrice = jsonData["dataset"]["data"][d][2]
    LowPrice = jsonData["dataset"]["data"][d][3]
    
    Diff = round(HighPrice - LowPrice, 2)
    AllPriceDiff.append(Diff)
        
max(AllPriceDiff)#2.81


# 5. What was the largest change between two consecutive days (based on Closing Price)?
ClosingDiff = [0]

for d in range(0,254):
    ClosingPrice = jsonData["dataset"]["data"][d][4]
    PriorClosingPrice = jsonData["dataset"]["data"][d+1][4]

    Diff = ClosingPrice - PriorClosingPrice
    ClosingDiff.append(Diff)
            
print("Largest change between two consecutive days :", round(max(ClosingDiff), 1))


#5. What was the largest change between any two days (based on Closing Price)?
ClosingDiffAll = [35]

for d in range(0,254):
    ClosingPrice = jsonData["dataset"]["data"][d][4]
    ClosingDiffAll.append(ClosingPrice)
    
Large = max(ClosingDiffAll)
Small = min(ClosingDiffAll)
            
print("Largest change between any two days :", round(Large - Small, 1))


# 6. What was the average daily trading volume during this year?
TradingVolume = [0]

for d in range(0,254):
    Volume = jsonData["dataset"]["data"][d][6]
    
    #Diff = HighPrice - LowPrice
    TradingVolume.append(Volume)
        
Total2017 = sum(TradingVolume)
Avg2017 = Total2017/(len(TradingVolume)-1) #89299 Trading Volume per day

#----
#End





















