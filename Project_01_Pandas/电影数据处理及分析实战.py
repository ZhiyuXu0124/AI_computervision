import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#读取数据
data = pd.read_csv('F:/AI（CV）/CLASSDATA_第二门_Python快速掌握/项目01_电影数据处理及分析实战/爱奇艺视频数据.csv',engine='python')

def shujuqinxi(df):
#数据清洗 - 去除空值
    cols = df.columns.tolist()
    for col in cols:
        if data[col].dtype == 'object':
            data[col].fillna('缺失数据',inplace = True)
        else:
            data[col].fillna(0,inplace = True)
    return df


def changtime(df,*cols):
#数据清洗 - 时间标签转化
    for col in cols :
        df[col] = df[col].str.replace('年','-')
        df[col] = df[col].str.replace('月','-')
        df[col] = df[col].str.replace('日','')
        df[col] = pd.to_datetime(df[col])
    return df

data_cl = shujuqinxi(data)  #data_cl 为去除空值后的数据
data_ct = changtime(data_cl,'数据获取日期')#data_ct 为时间标签转化后的数据

#好评率计算
data_goodrank = data_ct.groupby('导演')[['好评数','评分人数']].sum()
data_goodrank['好评率'] = data_goodrank['好评数']/data_goodrank['评分人数']
goodrank = data_goodrank.sort_values(['好评率'],ascending= False)[:20]
plt.figure(1)
goodrank['好评率'].plot(figsize = (16,9),
                     title = '不同导演好评率TOP20',
                     width = 0.8,
                     kind = 'bar',
                     color = 'Green',
                     alpha = 0.4,
                     rot = 45,
                     grid = True,
                     ylim = [0.97,1])
plt.show()

data_p1 = data_ct[['导演','上映年份','整理后剧名']].drop_duplicates()
data_p1 = data_p1[data_p1['上映年份']>2000]
data_p1 = data_p1[data_p1['上映年份']<=2016]
data_p2 = data_ct.groupby('整理后剧名').sum()[['评分人数','好评数']]
data_p3 = pd.merge(data_p1,data_p2,left_on='整理后剧名',right_index=True)
data_p4 = data_p3.groupby('上映年份').sum()[['评分人数','好评数']]
plt.figure(2)
data_p4['评分人数'].plot.area(figsize = (16,9),title = '2001-2016年每年评价影视人数总量统计',
                         grid = True,
                         color = 'Green',
                         alpha = 0.8)
plt.show()

fig,axes = plt.subplots(4,4,figsize=(10,16))
start_year = 2001
for i in range(4):
    for j in range(4):
        data_eachyear = data_p3[data_p3['上映年份'] == start_year]
        data_eachyear[['评分人数','好评数']].boxplot(whis = 3,ax = axes[i,j])
        color = dict(boxes='DarkGreen', whiskers='DarkOrange', medians='DarkBlue', caps='Gray')
        axes[i,j].set_title('%s'%start_year)
        start_year +=1
plt.show()
