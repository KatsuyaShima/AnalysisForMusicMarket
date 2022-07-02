#音楽市場分析
import sys
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
import numpy as np
from pyparsing import col

#データ量が少ないので、手作業でデータフレームを作成する。
df_5guys=pd.DataFrame({'TotalPhysical':[7.6,6.8,6.0,5.8,5.6,5.2,4.7,4.5,4.3,5.0],
                 'Streaming':[1.0,1.4,1.9,2.8,4.7,6.6,9.3,11.4,13.6,16.9],
                 'DownloadsAndOtherDigitals':[4.4,4.4,4.0,3.8,3.2,2.6,1.7,1.5,1.2,1.1],
                 'TotalRevenue':[15.0,14.7,14.2,14.7,16.1,17.3,18.9,20.4,21.9,25.9]},
                 index=[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021])

#リストの下準備
Total=[]
Flow_Physical=[]
Flow_Streaming=[]
Flow_DownloadsAndOtherDigital=[]
Flow_TotalRevenue=[]

#成長性(前年比率)を考える
for l in range(0,9):
    if df_5guys.at[2013+l,'TotalPhysical']!=0:
        Flow_Physical.append(round(((df_5guys.at[2013+l,'TotalPhysical']/df_5guys.at[2013+l-1,'TotalPhysical']-1)*100),2))
    else:
        Flow_Physical.append(0)
    if df_5guys.at[2013+l,'Streaming']!=0:
        Flow_Streaming.append(round(((df_5guys.at[2013+l,'Streaming']/df_5guys.at[2013+l-1,'Streaming']-1)*100),2))
    else:
        Flow_Streaming.append(0)
    if df_5guys.at[2013+l,'DownloadsAndOtherDigitals']!=0:
        Flow_DownloadsAndOtherDigital.append(round(((df_5guys.at[2013+l,'DownloadsAndOtherDigitals']/df_5guys.at[2013+l-1,'DownloadsAndOtherDigitals']-1)*100),2))
    else:
        Flow_DownloadsAndOtherDigital.append(0)
    if df_5guys.at[2013+l,'TotalRevenue']!=0:
        Flow_TotalRevenue.append(round(((df_5guys.at[2013+l,'TotalRevenue']/df_5guys.at[2013+l-1,'TotalRevenue']-1)*100),2))
    else:
        Flow_TotalRevenue.append(0)
    
data_list1=[Flow_Physical,Flow_Streaming,Flow_DownloadsAndOtherDigital,Flow_TotalRevenue]

df_flow=pd.DataFrame(data_list1,
                    columns=[2013,2014,2015,2016,2017,2018,2019,2020,2021],
                    index=['TotalPhysical','Streaming','DownloadsAndOtherDigitals','TotalRevenue'])
df_flow=df_flow.transpose()

df_5guys.to_csv(f'/Users/katuy/Desktop/data/Global_Revenue.csv',encoding="shift-jis")
df_flow.to_csv(f'/Users/katuy/Desktop/data/Global_Flow.csv',encoding="shift-jis")
