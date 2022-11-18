#coding=utf-8
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line

txts = []
path = r'E:\\dev\\web\\pyqt\\reden1.txt'
with open(path,'r+',encoding='utf-8') as file:
    txts = file.readlines()

print(txts)

dic = {}
time = []
fast = []
slow = []

for l in txts:
    text = l.split(',')
    time.append(text[0].split('#')[1])
    fa = text[1].split('#')[1].strip()
    fast.append((fa))
    sl = (text[2].split('#')[1]).strip()
    slow.append((sl))
dic["time"]=time
dic["fast"]=fast
dic["slow"]=slow
print(dic)

#折线图的数据格式：x轴和y轴都是列表数据
song_list = [972, 685, 553, 852, 472, 257, 243, 1307, 320, 438]
album_list = [35, 52, 58, 76, 71, 37, 18, 108, 13, 23]
mv_list = [1344, 745, 603, 497, 267, 266, 368, 1207, 220, 244]
singer_list = time

def set_line():

    line = Line()
    line.width = "1200px"
    line.height="500px"
    line.add_xaxis(xaxis_data = singer_list)
    #添加y轴数据，加上series_name，表示图例
    line.add_yaxis(series_name = '快线',y_axis = fast)
    line.add_yaxis(series_name = '慢线',y_axis = slow)

    line.set_global_opts(
        #设置图例形状
        legend_opts=opts.LegendOpts(legend_icon='pin'),
        #设置图表主标题，副标题和标题位置
        title_opts=opts.TitleOpts(title = '双均线',subtitle='走势',pos_left='20%'),
        #添加坐标轴名称，位置以及大小，name_gap表示名称与x轴距离，font_size是字体大小
        xaxis_opts = opts.AxisOpts(name = '时间',name_location='center',name_gap=25,name_textstyle_opts=opts.TextStyleOpts(font_size = 20)),
        yaxis_opts = opts.AxisOpts(name = '价格',min_='dataMin'),
        datazoom_opts = opts.DataZoomOpts(range_start=10,range_end=30), # 坐标轴进行缩放
        )

    return line

line = set_line()
line.render('xian4.html')
