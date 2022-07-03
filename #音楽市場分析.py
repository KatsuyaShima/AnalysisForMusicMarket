#音楽市場分析_Japan
import sys
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
import numpy as np
from pyparsing import col

#計算した値を元にデータフレームを作成(日本)
df_5guys=pd.DataFrame({'TotalPhysical':[3108,2705,2542,2544,2457,2320,2403,2291,1944,1936],
                 'Streaming':[10,31,79,124,200,263,349,465,589,744],
                 'DownloadsAndOtherdigitals':[533,386,359,347,329,310,296,241,193,151]},
                 index=[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021])

#リストの下準備
Total=[]
Flow_TotalPhysical=[]
Flow_Streaming=[]
Flow_TotalRevenue=[]
Flow_DownloadsAndOtherdigitals=[]

#トータル収益を算出しdataframe列に加える
for l in range(0,14):
    Total.append(df_5guys.at[2012+l,'TotalPhysical']+df_5guys.at[2012+l,'Streaming']+df_5guys.at[2012+l,'DownloadsAndOtherdigitals'])

#totalrevenue列を加える
df_5guys["TotalRevenue"] = Total

#成長性(前年比率)を考える
for l in range(0,13):
    if df_5guys.at[2013+l,'TotalPhysical']!=0:
        Flow_TotalPhysical.append(round(((df_5guys.at[2013+l,'TotalPhysical']/df_5guys.at[2013+l-1,'TotalPhysical']-1)*100),2))
    else:
        Flow_TotalPhysical.append(0)
    if df_5guys.at[2013+l,'Streaming']!=0:
        Flow_Streaming.append(round(((df_5guys.at[2013+l,'Streaming']/df_5guys.at[2013+l-1,'Streaming']-1)*100),2))
    else:
        Flow_Streaming.append(0)
    if df_5guys.at[2013+l,'DownloadsAndOtherdigitals']!=0:
        Flow_DownloadsAndOtherdigitals.append(round(((df_5guys.at[2013+l,'DownloadsAndOtherdigitals']/df_5guys.at[2013+l-1,'DownloadsAndOtherdigitals']-1)*100),2))
    else:
        Flow_DownloadsAndOtherdigitals.append(0)
    if df_5guys.at[2013+l,'TotalRevenue']!=0:
        Flow_TotalRevenue.append(round(((df_5guys.at[2013+l,'TotalRevenue']/df_5guys.at[2013+l-1,'TotalRevenue']-1)*100),2))
    else:
        Flow_TotalRevenue.append(0)
    
data_list1=[Flow_TotalPhysical,Flow_Streaming,Flow_DownloadsAndOtherdigitals,Flow_TotalRevenue]

df_flow=pd.DataFrame(data_list1,
                    columns=[2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025],
                    index=['TotalPhysical','Streaming','DownloadsAndOtherdigitals','TotalRevenue'])
df_flow=df_flow.transpose()

df_5guys.to_csv(f'/Users/katuy/Desktop/data/Japan_Revenue.csv',encoding="shift-jis")
df_flow.to_csv(f'/Users/katuy/Desktop/data/Japan_Flow.csv',encoding="shift-jis")
