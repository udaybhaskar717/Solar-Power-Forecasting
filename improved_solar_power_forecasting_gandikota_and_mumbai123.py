# -*- coding: utf-8 -*-
"""Improved_Solar_power_Forecasting_Gandikota_and_Mumbai123.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1twOTg_d5MRdtGIk-aCvTNtms3hykq9oh
"""

!python -m pip install opendatasets -U -qq
import opendatasets as od
import os
data_dir = os.getcwd()+"/data/"     #username	:	grudaykumarreddy
#key	:	76f7691f453416a26fb7bf445c9b3f3b
 #  


if not os.path.isdir(data_dir):
    od.download("https://www.kaggle.com/anikannal/solar-power-generation-data",data_dir=data_dir)
data_dir=os.getcwd()+"/data/solar-power-generation-data/"

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import zipfile

# Plant Generation Data
df_gen_1 = pd.read_csv('/content/data/solar-power-generation-data/Plant_1_Generation_Data.csv')      #Gandikota
df_gen_2 = pd.read_csv('/content/data/solar-power-generation-data/Plant_2_Generation_Data.csv')      #Nasik
# Plant Weather Data
df_weather_1 = pd.read_csv('/content/data/solar-power-generation-data/Plant_1_Weather_Sensor_Data.csv') 
df_weather_2= pd.read_csv('/content/data/solar-power-generation-data/Plant_1_Weather_Sensor_Data.csv')

df_gen_1

df_gen_1['DATE_TIME'] = pd.to_datetime(df_gen_1['DATE_TIME'], format='%d-%m-%Y %H:%M').dt.strftime('%Y-%m-%d %H:%M:%S')

df_gen_1

import pandas as pd
import plotly.express as px

df_gen_1['TIME'] =df_gen_1['DATE_TIME'].apply(lambda x:str(x)[-8:-3])

data_daily_averages = df_gen_1.groupby(['TIME','SOURCE_KEY']).mean().reset_index()
# data_daily_averages = data_daily_averages.groupby(['DATE_TIME']).mean().reset_index()


# Create plot
fig1 = px.line(data_daily_averages, x="TIME", y="AC_POWER", color="SOURCE_KEY", title="Daily Average AC Power by Inverter")
fig2 = px.line(data_daily_averages, x="TIME", y="DC_POWER", color="SOURCE_KEY", title="Daily Average DC Power by PV")
fig5 = px.line(data_daily_averages[data_daily_averages['TIME']<='18:15'], x="TIME", y="DAILY_YIELD", color="SOURCE_KEY", title="Daily Average DAILY_YILED Power by Inverter")
# Show plot
fig1.show()
fig2.show()
fig5.show()
df_gen_1.drop('TIME',axis=1,inplace=True)

df_gen_2

data_daily_averages



df_gen_2['TIME'] =df_gen_2['DATE_TIME'].apply(lambda x:str(x)[-8:-3])

data_daily_averages = df_gen_2.groupby(['TIME','SOURCE_KEY']).mean().reset_index()
# data_daily_averages = data_daily_averages.groupby(['DATE_TIME']).mean().reset_index()
# Create plot
fig3 = px.line(data_daily_averages, x="TIME", y="AC_POWER", color="SOURCE_KEY", title="Daily Average AC Power by Inverter")
fig4= px.line(data_daily_averages, x="TIME", y="DC_POWER", color="SOURCE_KEY", title="Daily Average DC Power PV")
fig6 = px.line(data_daily_averages, x="TIME", y="DAILY_YIELD", color="SOURCE_KEY", title="Daily Average DAILY_YILED Power by Inverter")
# Show plot
fig3.show()
fig4.show()
fig6.show()
df_gen_2.drop('TIME',axis=1,inplace=True)

df_weather_1

df_weather_2

print('Plant ID ',df_gen_1.PLANT_ID.unique())
print('No. of Inverters ',df_gen_1.SOURCE_KEY.nunique())
print('No. of Unique Source key',df_weather_1.SOURCE_KEY.nunique())
print('Null values in generation data: \n',df_gen_1.isnull().sum())
print('Null values in generation data: \n',df_weather_1.isnull().sum())

print('Plant ID ',df_gen_2.PLANT_ID.unique())
print('No. of Inverters ',df_gen_2.SOURCE_KEY.nunique())
print('No. of Unique Source key',df_weather_2.SOURCE_KEY.nunique())
print('Null values in generation data: \n',df_gen_2.isnull().sum())
print('Null values in generation data: \n',df_weather_2.isnull().sum())

Inverter_labels_1 = {inverter_no:inverter_name for inverter_name,inverter_no in enumerate(df_gen_1['SOURCE_KEY'].unique(),1)}
Inverter_labels_2 = {inverter_no:inverter_name for inverter_name,inverter_no in enumerate(df_gen_2['SOURCE_KEY'].unique(),1)}

#Dropping PLANT_ID 
df_gen_1.drop('PLANT_ID', axis=1, inplace=True)
df_weather_1.drop('PLANT_ID', axis = 1, inplace=True)

## Mapping
Inverter_labels_1 = {inverter_no:inverter_name for inverter_name,inverter_no in enumerate(df_gen_1['SOURCE_KEY'].unique(),1)}
df_gen_1['Inverter_No'] = df_gen_1['SOURCE_KEY'].map(Inverter_labels_1) 

## Drop Source Key after replacing with inverter numbers
df_gen_1.drop('SOURCE_KEY',axis=1,inplace=True)
df_weather_1.drop('SOURCE_KEY',axis=1,inplace=True) 
#Reordering and dropping Daily yield and Total yield
# df_gen_1 = df_gen_1[['DATE_TIME','Inverter_No' ,'DC_POWER', 'AC_POWER']]

#Dropping PLANT_ID 
df_gen_2.drop('PLANT_ID', axis=1, inplace=True)
df_weather_2.drop('PLANT_ID', axis = 1, inplace=True)

## Mapping
Inverter_labels_2 = {inverter_no:inverter_name for inverter_name,inverter_no in enumerate(df_gen_2['SOURCE_KEY'].unique(),1)}
df_gen_2['Inverter_No'] = df_gen_2['SOURCE_KEY'].map(Inverter_labels_2) 

## Drop Source Key after replacing with inverter numbers
df_gen_2.drop('SOURCE_KEY',axis=1,inplace=True)
df_weather_2.drop('SOURCE_KEY',axis=1,inplace=True) 
#Reordering and dropping Daily yield and Total yield
# df_gen_1 = df_gen_1[['DATE_TIME','Inverter_No' ,'DC_POWER', 'AC_POWER']]

print('Inverter {} has data for {} timestamps(Minimum)'.
      format(df_gen_1.groupby('Inverter_No')['DATE_TIME'].count().argmin()+1,df_gen_1.groupby('Inverter_No')['DATE_TIME'].count().min()))
print('Inverter {} has data for {} timestamps(Maximum)'.
      format(df_gen_1.groupby('Inverter_No')['DATE_TIME'].count().argmax()+1,df_gen_1.groupby('Inverter_No')['DATE_TIME'].count().max()))     
print('DIFFERENCE = {}'.format(df_gen_1.groupby('Inverter_No')['DATE_TIME'].count().max() - 
                               df_gen_1.groupby('Inverter_No')['DATE_TIME'].count().min()))

print('Inverter {} has data for {} timestamps(Minimum)'.
      format(df_gen_2.groupby('Inverter_No')['DATE_TIME'].count().argmin()+1,df_gen_2.groupby('Inverter_No')['DATE_TIME'].count().min()))
print('Inverter {} has data for {} timestamps(Maximum)'.
      format(df_gen_2.groupby('Inverter_No')['DATE_TIME'].count().argmax()+1,df_gen_2.groupby('Inverter_No')['DATE_TIME'].count().max()))     
print('DIFFERENCE = {}'.format(df_gen_2.groupby('Inverter_No')['DATE_TIME'].count().max() - 
                               df_gen_2.groupby('Inverter_No')['DATE_TIME'].count().min()))

from functools import reduce

grouped = df_gen_1.groupby('Inverter_No')

## Making a list of each Inverter group 
dfs_1 = list()
for i in df_gen_1['Inverter_No'].unique():
    dfs_1.append(grouped.get_group(i))

grouped = df_gen_2.groupby('Inverter_No')

## Making a list of each Inverter group 
dfs_2 = list()
for i in df_gen_2['Inverter_No'].unique():
    dfs_2.append(grouped.get_group(i))

dfs_1

dfs_2

df_new_1 = reduce(lambda left,right: pd.merge(left,right,on=['DATE_TIME'],how='outer'),dfs_1)
df_new_2 = reduce(lambda left,right: pd.merge(left,right,on=['DATE_TIME'],how='outer'),dfs_2)

df_new_1

df_new_2

columns_1=[('DC_POWER_'+str(x),'AC_POWER_'+str(x),'DAILY_YIELD_'+str(x),'TOTAL_YIELD_'+str(x),'Inverter_No_'+str(x)) for x in range(1,23)]
column_1=[]
for tu in columns_1:
    for column in tu:
        column_1.append(column)

columns_2=[('DC_POWER_'+str(x),'AC_POWER_'+str(x),'DAILY_YIELD_'+str(x),'TOTAL_YIELD_'+str(x),'Inverter_No_'+str(x)) for x in range(1,23)]
column_2=[]
for tu in columns_2:
    for column in tu:
        column_2.append(column)

## Merging data inverterwise using 'reduce'
 ## Applying merge function to all of the list elements of 'dfs' in the sequence passed.

#Rename columns
df_new_1.columns = ['DATE_TIME']+column_1
df_new_2.columns = ['DATE_TIME']+column_2

display(df_new_1)

display(df_new_2)

df_weather_1['DATE_TIME'] = df_weather_1['DATE_TIME'].astype(str)
df_weather_2['DATE_TIME'] = df_weather_2['DATE_TIME'].astype(str)
df_new_1['DATE_TIME'] = df_new_1['DATE_TIME'].astype(str)
df_new_2['DATE_TIME'] = df_new_2['DATE_TIME'].astype(str)
#Merging Generation & Weather datasets
df_1 = df_weather_1.merge(df_new_1,left_on='DATE_TIME',right_on='DATE_TIME',how='outer')
df_2 = df_weather_2.merge(df_new_2,left_on='DATE_TIME',right_on='DATE_TIME',how='outer')
#Generating 15 min time blocks
tb = pd.date_range('15-05-2020','16-05-2020',freq='15min')
tb=tb[:-1] 
ts = tb.strftime('%H:%M')
block_dict = {}
j=1
for i in range(len(ts)):
    block_dict[ts[i]] =  j
    j+=1

# Making new columns of Time,BLOCK and Date and droping DATE_TIME column
df_1['TIME'] = df_1['DATE_TIME'].apply(lambda x:str(x)[-8:-3])
df_2['TIME'] = df_2['DATE_TIME'].apply(lambda x:str(x)[-8:-3])

df_1['DATE'] = pd.to_datetime(df_1['DATE_TIME']).dt.date
df_2['DATE'] = pd.to_datetime(df_2['DATE_TIME']).dt.date
df_1['BLOCK'] = pd.to_datetime(df_1['TIME']).astype(str).apply(lambda x:block_dict[str(x)[-8:-3]])
df_2['BLOCK'] = pd.to_datetime(df_2['TIME']).astype(str).apply(lambda x:block_dict[str(x)[-8:-3]])
df_1.drop('DATE_TIME',axis=1,inplace=True)
df_2.drop('DATE_TIME',axis=1,inplace=True)
#Saving the dictionary using numpy
np.save('timestamp_block_dictionary.npy',block_dict)

## Column re-ordering
cols_1 = df_1.columns.tolist()
cols_2 = df_2.columns.tolist()

df_1 = df_1[[cols_1[-1]]+[cols_1[-2]]+[cols_1[-3]]+cols_1[:-3]]
df_2 = df_2[[cols_2[-1]]+[cols_2[-2]]+[cols_2[-3]]+cols_2[:-3]]
# display(df)

df_1

df_2

#Getting last 3 days data 
last_3_days_1 = df_1['DATE'].astype(str).unique()[-3:]
last_3_days_2= df_2['DATE'].astype(str).unique()[-3:]
df_test_1 = df_1[df_1['DATE'].astype(str).isin(last_3_days_1)].sort_values(by=['DATE','BLOCK'])
df_test_2 = df_2[df_2['DATE'].astype(str).isin(last_3_days_2)].sort_values(by=['DATE','BLOCK'])

#Saving Test data
df_test_1.reset_index(drop=True).to_csv('Test_data_1.csv')
df_test_2.reset_index(drop=True).to_csv('Test_data_2.csv')
#Saving all as Train for indexes not present in test data
df_train_1 = df_1[~df_1.index.isin(df_test_1.index)]
df_train_2 = df_2[~df_2.index.isin(df_test_2.index)]
df_train_1.to_csv('Train_data_1.csv')
df_train_2.to_csv('Train_data_2.csv')
## Checking shapes
print('Train_1:',df_train_1.shape)
print('Test_1:',df_test_1.shape)
print('Train_2:',df_train_2.shape)
print('Test_2:',df_test_2.shape)
## Check for missing values
print('No. of missing values in train dataset_1: ',list(df_train_1.isnull().sum()))
print('No. of missing values in train dataset_2: ',list(df_train_2.isnull().sum()))

f = plt.figure(figsize=(15,10))
ax1 = f.add_subplot(221)
ax2 = f.add_subplot(222)
ax3 = f.add_subplot(223)
ax4 = f.add_subplot(224)

ax1.plot(df_train_1[df_train_1['DATE'].astype(str)=='2020-05-18'].reset_index(drop=True)['DC_POWER_1'])
ax2.plot(df_train_1[df_train_1['DATE'].astype(str)=='2020-05-18'].reset_index(drop=True)['AMBIENT_TEMPERATURE'])
ax1.set_xlabel('Time Block_1')
ax1.set_ylabel('DC Power_1')

ax2.set_xlabel('Time Block_1')
ax2.set_ylabel('Ambient Temperature_1')

ax3.plot(df_train_2[df_train_2['DATE'].astype(str)=='2020-05-18'].reset_index(drop=True)['DC_POWER_1'])
ax4.plot(df_train_2[df_train_2['DATE'].astype(str)=='2020-05-18'].reset_index(drop=True)['AMBIENT_TEMPERATURE'])
ax3.set_xlabel('Time Block_2')
ax3.set_ylabel('DC Power_2')

ax4.set_xlabel('Time Block_2')
ax4.set_ylabel('Ambient Temperature_2')

plt.show()

#Code for Plot 1
df_12 = df_gen_1.copy() # Making a acopy 
df_22 = df_gen_2.copy() # Making a acopy 
df_12['DATE'] = pd.to_datetime(df_gen_1['DATE_TIME']).dt.date.astype(str)
df_22['DATE'] = pd.to_datetime(df_gen_2['DATE_TIME']).dt.date.astype(str)
## Selecting a date and replacing AC Power with NaN wherever its 0 and plotting 
indexes_1 = df_12[(df_12['Inverter_No']==1)&(df_12['DATE']=='2020-05-15')&(df_12['AC_POWER']==0)].index
indexes_2 = df_22[(df_22['Inverter_No']==1)&(df_22['DATE']=='2020-05-15')&(df_22['AC_POWER']==0)].index
df_12.loc[indexes_1,'AC_POWER']=np.nan
df_22.loc[indexes_2,'AC_POWER']=np.nan
df_12 = df_12[(df_12['Inverter_No']==1)&(df_12['DATE']=='2020-05-15')]['AC_POWER']
df_22 = df_22[(df_22['Inverter_No']==1)&(df_22['DATE']=='2020-05-15')]['AC_POWER']

df_12.plot();
df_22.plot();
#Code for Plot 2
## Comparison between 1 & 2 degree splines
fig_1, (ax1, ax2) = plt.subplots(1,2)
fig_2, (ax3, ax4) = plt.subplots(1, 2)
fig_1.suptitle('Degree = 1 and 2')
fig_2.suptitle('Degree = 1 and 2')
ax1.plot(df_12.interpolate(method='spline',order=1))
ax2.plot(df_12.interpolate(method='spline',order=2));

ax3.plot(df_22.interpolate(method='spline',order=1))
ax4.plot(df_22.interpolate(method='spline',order=2));

day_only_columns_1=list()
day_only_columns_2=list()
#Will collect all names like DC_POWER_1, DC_POWER_2 and so on 
DC_cols_1= [i for i in df_1.columns if 'DC_POWER' in i]
DC_cols_2 = [i for i in df_1.columns if 'DC_POWER' in i]
AC_cols_1= [i for i in df_2.columns if 'AC_POWER' in i]
AC_cols_2= [i for i in df_2.columns if 'AC_POWER' in i]
day_only_columns_1 = DC_cols_1+AC_cols_1+["IRRADIATION"]
day_only_columns_2 = DC_cols_2+AC_cols_2+["IRRADIATION"]
def Data_Preparation_Plant_Level(df_1,df_2):
    for col in day_only_columns_1:
        df_1[col] = df_1[col].astype(float)
        # For time except for non-generating hours(12 am to 6 am & 6 pm to 12 am) will be replaced by zero
        df_1.loc[df_1[(~((df_1['BLOCK']>24) & (df_1['BLOCK']<73))) & df_1[col].isnull()].index,col] = 0
    for col in day_only_columns_2:
        df_2[col] = df_2[col].astype(float)
        # For time except for non-generating hours(12 am to 6 am & 6 pm to 12 am) will be replaced by zero
        df_2.loc[df_2[(~((df_2['BLOCK']>24) & (df_2['BLOCK']<73))) & df_2[col].isnull()].index,col] = 0
    # Left NaN value for generating hours(6 am to 6pm) 
       
        #1.AC & DC columns
    df_1[DC_cols_1+AC_cols_1].interpolate(method='polynomial',order = 2,inplace=True)
    df_2[DC_cols_2+AC_cols_2].interpolate(method='polynomial',order = 2,inplace=True)
       #2.Left NaN values in Irradiation, Ambient Temp, Module Temp, Inverter_No
    df_1.interpolate(method='linear',inplace=True)
    df_2.interpolate(method='linear',inplace=True)
    
    # Summing up Inverter wise AC and DC values to reach Plant-level generation
    df_1['AC_POWER'] = df_1.loc[: ,AC_cols_1].sum(axis=1)
    df_2['AC_POWER'] = df_2.loc[: ,AC_cols_2].sum(axis=1)
    df_1['DC_POWER'] = df_1.loc[:,DC_cols_1].sum(axis=1)
    df_2['DC_POWER'] = df_2.loc[:,DC_cols_2].sum(axis=1)
    #Scaling generation to MW from kW  
    df_1['AC_POWER'] = df_1['AC_POWER']/1000
    df_2['AC_POWER'] = df_2['AC_POWER']/1000
    df_1['DC_POWER'] = df_1['DC_POWER']/1000
    df_2['DC_POWER'] = df_2['DC_POWER']/1000
    
    return (df_1,df_2)
#Applying the function on Train & Test 
df_train_1,df_train_2 = Data_Preparation_Plant_Level(df_train_1,df_train_2)
df_test_1,df_test_2 = Data_Preparation_Plant_Level(df_test_1,df_test_2)

import seaborn as sns
sns.pairplot(df_train_1[['AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE',
       'IRRADIATION','AC_POWER']],height=2.5)

sns.pairplot(df_train_2[['AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE',
       'IRRADIATION','AC_POWER']],height=2.5)

for feature in df_train_1.columns[3:]:
    # ignoring zero values for plotting
    df_train_1[df_train_1[feature]!=0].boxplot(column=feature)
    plt.ylabel(feature)
    plt.show()

for feature in df_train_2.columns[3:]:
    # ignoring zero values for plotting
    df_train_2[df_train_2[feature]!=0].boxplot(column=feature)
    plt.ylabel(feature)
    plt.show()

display(df_train_1.iloc[:,1:].corr())
plt.figure(figsize = (12,8))
sns.heatmap(df_train_1[['AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE', 'IRRADIATION',
       'AC_POWER', 'DC_POWER']].corr(),annot=True)

df_plant_2=df_train_2.copy()
df_plant_1=df_train_1.copy()

display(df_train_2.iloc[:,1:].corr())
plt.figure(figsize = (12,8))
sns.heatmap(df_train_2[['AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE', 'IRRADIATION',
       'AC_POWER', 'DC_POWER']].corr(),annot=True)

# df_train.drop('DC_POWER',axis=1,inplace=True)
percentile_dict_1 = {}
for i in df_train_1.columns[3:]:
    a_list = []
    for j in [1,10,25,50,75,90,99,100]:
        a_list.append(round(np.percentile(df_train_1[i],j),2))
    percentile_dict_1[i] = a_list    
pd.DataFrame(pd.concat([pd.DataFrame({'Percentiles':[1,10,25,50,75,90,99,100]}),pd.DataFrame(percentile_dict_1)],axis=1))

percentile_dict_2 = {}
for i in df_train_2.columns[3:]:
    a_list = []
    for j in [1,10,25,50,75,90,99,100]:
        a_list.append(round(np.percentile(df_train_2[i],j),2))
    percentile_dict_2[i] = a_list    
pd.DataFrame(pd.concat([pd.DataFrame({'Percentiles':[1,10,25,50,75,90,99,100]}),pd.DataFrame(percentile_dict_2)],axis=1))

df_train_1=df_train_1[['BLOCK','DATE','TIME','AMBIENT_TEMPERATURE','MODULE_TEMPERATURE','IRRADIATION','AC_POWER','DC_POWER']]
df_train_2=df_train_2[['BLOCK','DATE','TIME','AMBIENT_TEMPERATURE','MODULE_TEMPERATURE','IRRADIATION','AC_POWER','DC_POWER']]
df_test_1=df_test_1[['BLOCK','DATE','TIME','AMBIENT_TEMPERATURE','MODULE_TEMPERATURE','IRRADIATION','AC_POWER','DC_POWER']]
df_test_2=df_test_2[['BLOCK','DATE','TIME','AMBIENT_TEMPERATURE','MODULE_TEMPERATURE','IRRADIATION','AC_POWER','DC_POWER']]

outlier_imputer_dict_1= {}

for var in df_train_1.columns[3:]:
    percentile_dict_1 = {}
    
    NinetyNine_percentile = np.percentile(df_train_1[var],99)  
       
    First_percentile = np.percentile(df_train_1[var],1)

    percentile_dict_1['99th'] =  NinetyNine_percentile
    percentile_dict_1['1st'] =  First_percentile  
    # Saving as dictionary for each column
    outlier_imputer_dict_1[var] = percentile_dict_1

outlier_imputer_dict_2= {}

for var in df_train_2.columns[3:]:
    percentile_dict_2 = {}
    
    NinetyNine_percentile = np.percentile(df_train_2[var],99)  
       
    First_percentile = np.percentile(df_train_2[var],1)

    percentile_dict_2['99th'] =  NinetyNine_percentile
    percentile_dict_2['1st'] =  First_percentile  
    # Saving as dictionary for each column
    outlier_imputer_dict_2[var] = percentile_dict_2

outlier_imputer_dict_1

outlier_imputer_dict_2

#Saving the final dictionary         
np.save('outlier_imputer_dict_1',outlier_imputer_dict_1)   
np.save('outlier_imputer_dict_2',outlier_imputer_dict_2)

def outlier_imputer(df_1,df_2):
    #Loading Outlier Imputer dictionary
    outlier_dict_1 = np.load('outlier_imputer_dict_1.npy',allow_pickle='TRUE').item()
    outlier_dict_2 = np.load('outlier_imputer_dict_2.npy',allow_pickle='TRUE').item()
    print(df_1.columns[3:])
    print(df_2.columns[3:])
    for var in df_1.columns[3:]:
        
        df_1.loc[df_1[df_1[var] > outlier_dict_1[var]['99th']].index,var] = outlier_dict_1[var]['99th']  
       
        df_1.loc[df_1[df_1[var] < outlier_dict_1[var]['1st']].index,var] = outlier_dict_1[var]['1st']
    for var in df_2.columns[3:]:
        
        df_2.loc[df_2[df_2[var] > outlier_dict_2[var]['99th']].index,var] = outlier_dict_2[var]['99th']  
       
        df_2.loc[df_2[df_2[var] < outlier_dict_2[var]['1st']].index,var] = outlier_dict_2[var]['1st']    
    return (df_1,df_2)



#Applying imputation on Train & Test 
df_train_1,df_train_2 = outlier_imputer(df_train_1,df_train_2)
df_test_1,df_test_2 = outlier_imputer(df_test_1,df_test_2)

print(outlier_imputer_dict_1)

#No. of bins
cut_blocks = [1,2,3,4,5,6,7,8]
#Bins range
cut_bins =[0, 12, 24, 36, 48, 60, 72, 84, 96]
#Assigning each row to a bin based on BLOCKS
df_train_1['BIN'] = pd.cut(df_train_1['BLOCK'], bins=cut_bins, labels = cut_blocks)
display(df_train_1)

df_train_2['BIN'] = pd.cut(df_train_2['BLOCK'], bins=cut_bins, labels = cut_blocks)
display(df_train_2)

df_train_1.drop('DC_POWER',axis=1,inplace=True)
df_test_1.drop('DC_POWER',axis=1,inplace=True)
df_train_2.drop('DC_POWER',axis=1,inplace=True)
df_test_2.drop('DC_POWER',axis=1,inplace=True)

#Splitting train into x & y
x_train_1 = df_train_1[['AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE',
       'IRRADIATION']]
y_train_1 = df_train_1[['AC_POWER']]

x_valid_1 = df_test_1[['AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE',
       'IRRADIATION']]
y_valid_1 = df_test_1[['AC_POWER']]

x_train_2 = df_train_2[['AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE',
       'IRRADIATION']]
y_train_2 = df_train_2[['AC_POWER']]

x_valid_2 = df_test_2[['AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE',
       'IRRADIATION']]
y_valid_2 = df_test_2[['AC_POWER']]

"""# Plant_1"""

import warnings
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import LeaveOneOut, RepeatedKFold, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import BaggingRegressor, AdaBoostRegressor
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.utils import resample
from sklearn.metrics import make_scorer
from sklearn.base import BaseEstimator
import numpy as np

# Creating a dictionary of models
models = {
    'Linear Regression': LinearRegression(),
    'KNN': KNeighborsRegressor(),
    'SVR': SVR(),
    'Decision Tree': DecisionTreeRegressor(),
    'Random Forest': RandomForestRegressor(),
    'Gradient Boosting': GradientBoostingRegressor(),
}

# Creating a dictionary of pipelines
pipelines = {
    'sc_LR': Pipeline([('Scaler', StandardScaler()), ('LR', LinearRegression())]),
    'sc_KNN': Pipeline([('Scaler', StandardScaler()), ('KNN', KNeighborsRegressor())]),
    'sc_SVR': Pipeline([('Scaler', StandardScaler()), ('SVR', SVR())]),
    'mm_DT': Pipeline([('Scaler', MinMaxScaler()), ('DT', DecisionTreeRegressor())]),
    'mm_RF': Pipeline([('Scaler', MinMaxScaler()), ('RF', RandomForestRegressor())]),
    'mm_GB': Pipeline([('Scaler', MinMaxScaler()), ('GB', GradientBoostingRegressor())]),
}

# Defining the parameters for GridSearchCV
param_grid = {
    'LR': {'LR__fit_intercept': [True, False], 'LR__normalize': [True, False]},
    'KNN': {'KNN__n_neighbors': np.arange(1, 31), 'KNN__weights': ['uniform', 'distance']},
    'SVR': {'SVR__C': np.logspace(-3, 3, 7), 'SVR__kernel': ['linear', 'poly', 'rbf', 'sigmoid']},
    'DT': {'DT__max_depth': np.arange(1, 11), 'DT__min_samples_split': np.arange(2, 11)},
    'RF': {'RF__n_estimators': np.arange(10, 110, 10), 'RF__max_depth': np.arange(1, 11)},
    'GB': {'GB__n_estimators': np.arange(10, 110, 10), 'GB__learning_rate': np.linspace(0.1, 1, 10), 'GB__max_depth': np.arange(1, 11)}
}

# Initialize variables to store the best model and best RMSE
best_rmse = float('inf')
best_model = None
best_pipeline = None
best_grid_search = None

# Initialize a dictionary to store the mean RMSE for each model
mean_rmse = {}

# Initialize a dictionary to store the mean R2 for each model
mean_r2 = {}

# Define the evaluation metric
scorer = make_scorer(mean_squared_error, greater_is_better=False)

# Iterate through the models and pipelines
for name, model in models.items():
    for pipe_name, pipeline in pipelines.items():
        # Check if the current pipeline contains the current model
        if model in pipeline.named_steps.values():
            # Get the prefix of the pipeline (e.g. 'sc_' for the 'sc_LR' pipeline)
            prefix = pipe_name.split("_")[0]
            # Get the model name without the prefix (e.g. 'LR' for the 'sc_LR' pipeline)
            model_name = pipe_name.split("_")[1]
            # Check if the current model has a corresponding entry in the param_grid
            if model_name in param_grid:
                # Create an instance of GridSearchCV
                grid_search = GridSearchCV(pipeline, param_grid[model_name], cv=5, scoring=scorer, n_jobs=-1, return_train_score=True)
                # Fit the grid search to the data
                grid_search.fit(x_train_1, y_train_1)
                # Get the mean RMSE for the current model and pipeline
                rmse = np.sqrt(-grid_search.cv_results_['mean_test_score'].mean())
                r2 = r2_score(y_valid_1, grid_search.predict(x_valid_1))
                # Add the mean RMSE to the dictionary
                mean_rmse[pipe_name] = rmse
                mean_r2[pipe_name] = r2
                # Print the results
                print(f'{pipe_name} - RMSE: {rmse:.4f} R2: {r2:.4f}')
                # Update the best model and best RMSE if necessary
                if rmse < best_rmse:
                    best_rmse = rmse
                    best_model = model
                    best_pipeline = pipeline
                    best_grid_search = grid_search

print(f'\nBest model: {best_model}')
print(f'Best pipeline: {best_pipeline}')
print(f'Best grid search: {best_grid_search}')
print(f'Best RMSE: {best_rmse:.4f}')

# Using ensemble method
bag_reg = BaggingRegressor(best_model, n_estimators=100, bootstrap=True, bootstrap_features=True, oob_score=True)
bag_reg.fit(x_train_1,y_train_1)
y_pred = bag_reg.predict(x_valid_1)
bag_rmse = np.sqrt(mean_squared_error(y_valid_1, y_pred))
bag_r2 = r2_score(y_valid_1, y_pred)
print(f'Bagging Regressor RMSE: {bag_rmse:.4f} R2: {bag_r2:.4f}')

ada_reg = AdaBoostRegressor(best_model, n_estimators=100, learning_rate=0.1)
ada_reg.fit(x_train_1, y_train_1)
y_pred = ada_reg.predict(x_valid_1)
ada_rmse = np.sqrt(mean_squared_error(y_valid_1, y_pred))
ada_r2 = r2_score(y_valid_1, y_pred)
print(f'AdaBoost Regressor RMSE: {ada_rmse:.4f} R2: {ada_r2:.4f}')

# Using stacking method
estimators = [('LR', LinearRegression()), ('RF', RandomForestRegressor()), ('GB', GradientBoostingRegressor())]
stack_reg_1 = StackingRegressor(estimators=estimators, final_estimator=LinearRegression())
stack_reg_1.fit(x_train_1, y_train_1)
y_pred = stack_reg_1.predict(x_valid_1)
stack_rmse = np.sqrt(mean_squared_error(y_valid_1, y_pred))
stack_r2 = r2_score(y_valid_1, y_pred)
print(f'Stacking Regressor RMSE: {stack_rmse:.4f} R2: {stack_r2:.4f}')

# Compare the performance of the ensemble methods with the best model
if bag_rmse < best_rmse:
    best_rmse = bag_rmse
    best_model = "Bagging Regressor"
if ada_rmse < best_rmse:
    best_rmse = ada_rmse
    best_model = "AdaBoost Regressor"
if stack_rmse < best_rmse:
    best_rmse = stack_rmse
    best_model = "Stacking Regressor"

print(f'\nBest Ensemble model: {best_model}')
print(f'Best Ensemble RMSE: {best_rmse:.4f}')

"""# Deploying the model

## Importing the libraries
"""

pip install streamlit

import pickle
import streamlit as st

# Save the model to disk
with open('solar_power_forecasting_model.pkl', 'wb') as file:
    pickle.dump(stack_reg_1, file)

x_train_1

# Load the pre-trained model
model = pickle.load(open('solar_power_forecasting_model.pkl', 'rb'))

# Create the Streamlit app
st.set_page_config(page_title='Solar Power Forecasting', page_icon=':sunny:')
st.title('Solar Power Forecasting')

# Create the user interface
st.sidebar.header('Enter the data')
st.sidebar.subheader('Date and time')
date_time = st.sidebar.date_input('Date')
hour = st.sidebar.slider('Hour', 0, 23)
st.sidebar.subheader('Weather information')
AmbientTemperature = st.sidebar.number_input('Ambient Temperature (°C)')
ModuleTemperature = st.sidebar.number_input('Module Temperature (°C)')
Irradiance = st.sidebar.number_input('Irradiance (W/m^2)')
# humidity = st.sidebar.slider('Humidity (%)', 0, 100)
# wind_speed = st.sidebar.number_input('Wind speed (m/s)')
# wind_direction = st.sidebar.number_input('Wind direction (°)')
# cloud_cover = st.sidebar.number_input('Cloud cover (%)')
# st.sidebar.subheader('Additional information')
# pressure = st.sidebar.number_input('Pressure (hPa)')

# Make the prediction
if st.sidebar.button('Predict'):
    data = pd.DataFrame({
        'year': [date_time.year],
        'month': [date_time.month],
        'day': [date_time.day],
        'hour': [hour],
        'Ambient_Temperature': [AmbientTemperature],
        'Module_Temperature': [ModuleTemperature],
        'Irradiance': [Irradiance]
    })
    prediction = model.predict(data[['Ambient_Temperature','Module_Temperature','Irradiance']])[0]
    st.success(f'The predicted solar power production is {prediction:.2f} kW')

! streamlit run app.py

