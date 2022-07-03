#MakingGragh
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
from datetime import datetime as dt
import numpy as np
from pyparsing import col

#音楽市場分析で作成したcsvデータの読み込み
df_Segments=pd.read_csv(f'/Users/katuy/Desktop/data/Japan_Revenue.csv',encoding="shift-jis")

# === グラフ描画：開始 ================================================
fig, ax = plt.subplots()
plt.vlines(9, 0, 5000, colors='black', linestyle='dashed', linewidth=3)

x1 = df_Segments.index.tolist()
y1 = df_Segments['TotalRevenue'].values
x2 = df_Segments.index.tolist()
y2 = df_Segments['TotalPhysical'].values
x3 = df_Segments.index.tolist()
y3 = df_Segments['Streaming'].values
x4 = df_Segments.index.tolist()
y4 = df_Segments['Downloads'].values

c1,c2,c3,c4 = "#03AF7A","#4DC4FF","#F6AA00","#AA4499" # 各プロットの色

#ax.set_title('Japanese Recorded Music Industry Revenues 2005-2025') # グラフタイトル
#ax.set_xlabel('Years')  # x軸ラベル
#ax.set_ylabel('Hundred Million Yen')  # y軸ラベル
#ax.set_xticks(list(range(0,len(oya_data),2)))
# ax.set_aspect('equal') # スケールを揃える
ax.grid(color='b', linestyle=':', linewidth=0.3) # 罫線
ax.set_xlim([0, 10]) # x方向の描画範囲を指定
ax.set_ylim([0, 30])    # y方向の描画範囲を指定
ax.plot(x1, y1, color=c1)#, label=l1)
ax.plot(x2, y2, color=c2)#, label=l2)
ax.plot(x3, y3, color=c3)#, label=l3)
ax.plot(x4, y4, color=c4)#, label=l3)

#ax.legend(loc=0)    # 凡例
#fig.tight_layout()  # レイアウトの設定
#plt.xticks(fontsize=6)
plt.xticks([0,1,2,3,4,5,6,7,8,9], [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021])
plt.xticks(rotation=90)

plt.savefig('/Users/katuy/Desktop/'+str("Japan_Revenue")+'.png') # 画像の保存
plt.clf()
plt.close(fig)
# === グラフ描画：終了 ===============================================
  
