

import csv
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
from sklearn.linear_model import LinearRegression

parking = pd.read_csv('/Users/Suha/Projects/TestGitHub/Parking_ticket/Parking_Citations.csv' , low_memory = False)

## For all citations, what is the mean violation fine?

parking['ViolFine'].mean(skipna = True)

#49.89393827148787



## Looking only at vehicles that have open penalty fees, what dollar amount is the 81st percentile of that group?

parking[parking['OpenPenalty'] != 0]['OpenPenalty'].describe(percentiles = [.81])

##Find the police district that has the highest mean violation fine. What is that mean violation fine? Keep in mind that Baltimore is divided into nine police districts, so clean the data accordingly.
mapping_dict =   {'Southeastern':'SOUTHEASTERN'
                ,  'Southern': 'SOUTHERN'
                , 'Southwestern':'SOUTHWESTERN'
                , 'Western':'WESTERN'
                ,  'Northwestern': 'NORTHWESTERN'
                ,  'Northern':'NORTHERN'
                , 'Notheastern':'NORTHEASTERN'
                ,  'Eastern' :'EASTERN'
                ,  'Central':'CENTRAL'
               }
parking['PoliceDistrict'] = parking['PoliceDistrict'].map(mapping_dict)

# of the not null values, we will do the analysis to find out the hightest mean violation fine

district = ['SOUTHEASTERN','SOUTHERN','CENTRAL','NORTHERN','NORTHEASTERN','EASTERN','SOUTHWESTERN','WESTERN','NORTHWESTERN']

distict_fine = []
for name in district:
    parking_subset = parking[parking['PoliceDistrict'] == name]
    parking_subset_mean_fine = parking_subset['ViolFine'].mean()
    distict_fine.append((name,parking_subset_mean_fine))
max(distict_fine)
    #('WESTERN', 53.02462620932278)


##  Find the ten vehicle makes that received the most citations during 2017. For those top ten, find all Japanese-made vehicles. What proportion of all citations were written for those vehicles? Note that the naming in Make is not consistent over the whole dataset, so you will need to clean the data before calculating your answer. Your answer should be expressed as a decimal number (i.e. 0.42, not 42).

## not completed
## First, find the total number of citations given in each year between 2004 and 2014 (inclusive). Next, using linear regression, create a function that plots the total number of citations as a function of the year. If you were to plot a line using this function, what would be the slope of that line?


## extract year from the date - takes time see if modification possible
parking['Viol_Year'] = parking['ViolDate'].str.split(" ", expand = True)[0].str.split("/", expand = True)[2]

# filtering appropriate year
parking_violation = parking[(parking['Viol_Year'] < '2015') & (parking['Viol_Year'] > '2003')]

# group by violation year
violation_citation = parking_violation[['Viol_Year' , 'Citation']].groupby('Viol_Year').count().reset_index()

# prepare the variables for regression
X = violation_citation['Viol_Year'].values.reshape(-1, 1).astype(float)
Y = violation_citation['Citation'].values.reshape(-1, 1)

lr = LinearRegression()
reg = lr.fit(X,Y)
# print(reg.intercept_ ) # intercept
print(reg.coef_) # slope
Y_pred = lr.predict(X)  # make prediction

# [[ 11220.09090909]]

## First, determine how many instances of auto theft ocurred in each police district during 2015. Next, determine the number of parking citations that were issued in each police district during the same year. Finally, determine the ratio of auto thefts to parking citations for each district. Out of the nine police districts, what was the highest ratio?

crime = pd.read_csv('/Users/Suha/Projects/TestGitHub/Parking_ticket/BPD_Part_1_Victim_Based_Crime_Data.csv' , low_memory = False)

crime['CrimeYear'] = crime['CrimeDate'].str.split("/", expand = True)[2]

mapping_dict =   {'SOUTHEAST':'SOUTHEASTERN'
                ,  'SOUTHERN': 'SOUTHERN'
                , 'SOUTHWEST':'SOUTHWESTERN'
                , 'WESTERN':'WESTERN'
                ,  'NORTHWEST': 'NORTHWESTERN'
                ,  'NORTHERN':'NORTHERN'
                , 'NORTHEAST':'NORTHEASTERN'
                ,  'EASTERN' :'EASTERN'
                ,  'CENTRAL':'CENTRAL'
               }
crime['District'] = crime['District'].map(mapping_dict)


#total auto theft in each police district in 2015
crime_auto_theft_2015 = crime[(crime['CrimeYear'] =='2015')&(crime['Description']=='AUTO THEFT')]
crime_by_district = crime_auto_theft_2015 [['District' ,'Total Incidents' ]].groupby('District').sum()

#total parking citations  in each police district in 2015
parking_2015 = parking[(parking['Viol_Year'] =='2015')]
parking_by_district = parking_2015 [['PoliceDistrict' ,'Citation' ]].groupby('PoliceDistrict').count()
ratio_df = pd.merge(left = crime_by_district , right = parking_by_district , left_index = True , right_index = True)
ratio_df['incidents_to_tickets'] = ratio_df['Total Incidents']/ratio_df['Citation'].astype(float)
ratio_df['incidents_to_tickets'].max()
