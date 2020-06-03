# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:57:47 2020

@author: AHS
"""

#The attached logins.json file contains (simulated) timestamps of user logins in a particular
#geographic location. 

import json
logins = "C:/Users/abulh/Sync/O4_P1_SpringBoardMLCourse/Unit18/1481053515_ultimate_challenge/ultimate_challenge/logins.json"
        
import pandas as pd
from datetime import datetime
import time
loginsDF = pd.read_json (logins)
loginsDF["login_time"] = pd.to_datetime(loginsDF["login_time"])
loginsDF['year'] = loginsDF['login_time'].dt.year
loginsDF['month'] = loginsDF['login_time'].dt.month
loginsDF['day'] = loginsDF['login_time'].dt.day
loginsDF['hour'] = loginsDF['login_time'].dt.hour
loginsDF['minute'] = loginsDF['login_time'].dt.minute
loginsDF['minute'][loginsDF['minute']<15] = 14
loginsDF['minute'][(loginsDF['minute'] >= 15) & (loginsDF['minute']<30)] = 29
loginsDF['minute'][(loginsDF['minute'] >= 30) & (loginsDF['minute']<45)] = 44
loginsDF['minute'][(loginsDF['minute'] >= 45) & (loginsDF['minute']<60)] = 59


#Aggregate these login counts based on 15­minute time intervals, 
loginsDF = loginsDF.groupby(["year", "month", "day", "hour", "minute"]).agg("count").reset_index()
loginsDF['timestamp'] = (loginsDF["year"].astype(str)+"-"+
                         loginsDF["month"].astype(str)+"-"+
                         loginsDF["day"].astype(str)+" "+
                         loginsDF["hour"].astype(str)+":"+
                         loginsDF["minute"].astype(str)+":00")

loginsDF = loginsDF.set_index('timestamp')
loginsTS = loginsDF["login_time"]

#visualize and describe the resulting time series of login counts in ways that best characterize the
#underlying patterns of the demand. 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(11, 4)})
loginsTS.plot(linewidth=0.5);


#Please report/illustrate important features of the demand,
#such as daily cycles. If there are data quality issues, please report them.

#There appears to be a three month worth of data.
#The The amount of consumer behaviour appears to increase over the span of the
#three months.


#-----------------------
import json
UDC = "C:/Users/abulh/Sync/O4_P1_SpringBoardMLCourse/Unit18/1481053515_ultimate_challenge/ultimate_challenge/ultimate_data_challenge.json"
UDCdf = pd.read_json (UDC)


UDCdf.groupby("city").agg("count")
#three cities, Astapor & King's Landing havd ~12k users, 
#Winterfell has 10K more
UDCdf['city'] = UDCdf['city'].astype('category')
dum_city = pd.get_dummies(UDCdf["city"], columns=["city"], prefix="city" )
UDCdf = UDCdf.join(dum_city)


UDCdf.groupby("phone").agg("count")
#Two phones, twice as man iphone users as andrioid
UDCdf['phone'] = UDCdf['phone'].astype('category')
dum_phone = pd.get_dummies(UDCdf["phone"], columns=["phone"], prefix="phone" )
UDCdf = UDCdf.join(dum_phone)

UDCdf.groupby("signup_date").agg("count")
#Sign up date was Jan 2014, apx even distribution accross all days
#There seems to be a periodic type behaviour. If introduce weekdays, 
#Maybe could use as feature...I am leaning towards a multivariable regression
#where I back eliminate to find the sig variables. 
UDCdf["signup_date"] = pd.to_datetime(UDCdf["signup_date"])
UDCdf["signup_day"] = UDCdf["signup_date"].dt.weekday
UDCdf['signup_day'] = UDCdf['signup_day'].astype('category')
dum_signup_day = pd.get_dummies(UDCdf["signup_day"], columns=["signup_day"], prefix="signup_day" )
UDCdf = UDCdf.join(dum_signup_day)


A = UDCdf.groupby("last_trip_date").agg("count")
#Majority of the users have a last trip date 5-6 months later, but
#there are quite a few users who drop off within the first month.
#The day difference between sigining up and last trip can be used as a output 
#With the objective of identifying which factors increase the retention.
UDCdf["last_trip_date"] = pd.to_datetime(UDCdf["last_trip_date"])
UDCdf["daysSignedup"] = (UDCdf["last_trip_date"] - UDCdf["signup_date"]).dt.days

UDCdf.groupby("avg_dist").agg("count")
#Majority of the distance traveled is less than 20 units.


UDCdf.groupby("avg_rating_by_driver").agg("count")
UDCdf["avg_rating_by_driver"] = UDCdf["avg_rating_by_driver"].fillna(UDCdf["avg_rating_by_driver"].mean())

UDCdf.groupby("avg_rating_of_driver").agg("count")
UDCdf["avg_rating_of_driver"] = UDCdf["avg_rating_of_driver"].fillna(UDCdf["avg_rating_of_driver"].mean())

#Majority of the raitings are 5start, but lets still use feature.


UDCdf.groupby("trips_in_first_30_days").agg("count")
#majority of the users took a trip within the first 30 days

UDCdf.groupby("ultimate_black_user").agg("count")
#~70% are not black users
UDCdf['ultimate_black_user'] = UDCdf['ultimate_black_user'].astype('category')
dum_ultimate_black_user = pd.get_dummies(UDCdf["ultimate_black_user"], columns=["ultimate_black_user"], prefix="ultimate_black_user" )
UDCdf = UDCdf.join(dum_ultimate_black_user)

UDCdf.groupby("weekday_pct").agg("mean")
#lets use this also as a feature

#Now that I have a sense of the data, lets modify the features so I can use
#them in the multivariable regression.

list(UDCdf.columns)

#Input Variable
# split the dataframe into dependent and independent variables.  
All = UDCdf[[
            "daysSignedup",
            'trips_in_first_30_days',
            'avg_rating_of_driver',
            'avg_surge',
            'surge_pct',
            'ultimate_black_user_False',
            'ultimate_black_user_True',
            'weekday_pct',
            'avg_dist',
            'avg_rating_by_driver',
            'city_Astapor',
            "city_King's Landing",
            'city_Winterfell',
            'phone_Android',
            'phone_iPhone',
            'signup_day_0',
            'signup_day_1',
            'signup_day_2',
            'signup_day_3',
            'signup_day_4',
            'signup_day_5',
            'signup_day_6'
    ]] 
All.corr()

x = UDCdf[[
            'trips_in_first_30_days',
            'avg_rating_of_driver',
            'avg_surge',
            'surge_pct',
            'ultimate_black_user_False',
            'ultimate_black_user_True',
            'weekday_pct',
            'avg_dist',
            'avg_rating_by_driver',
            'city_Astapor',
           "city_King's Landing",
            'city_Winterfell',
#            'phone_Android',
            'phone_iPhone',
            'signup_day_0',
            'signup_day_1',
            'signup_day_2',
            'signup_day_3',
            'signup_day_4',
            'signup_day_5',
            'signup_day_6'
    ]] 
 


#Explanatory Variable
y = UDCdf['daysSignedup'] 


import statsmodels.regression.linear_model as sm 
ols = sm.OLS(endog = y, exog = x).fit() 
ols.summary() 













