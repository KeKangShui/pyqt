from pyecharts import options as opts
from pyecharts.charts import Line

#折线图的数据格式：x轴和y轴都是列表数据
song_list = [972, 685, 553, 852, 472, 257, 243, 1307, 320, 438]
album_list = [35, 52, 58, 76, 71, 37, 18, 108, 13, 23]
mv_list = [1344, 745, 603, 497, 267, 266, 368, 1207, 220, 244]
singer_list = ['周杰伦','林俊杰','王力宏','张杰','汪苏泷','许嵩','薛之谦','陈奕迅','李荣浩','陶喆']

def set_line():
    line = Line()
    line.add_xaxis(xaxis_data = singer_list)
    #添加y轴数据，加上series_name，表示图例
    line.add_yaxis(series_name = '单曲',y_axis = song_list)
    line.add_yaxis(series_name = 'MV',y_axis = mv_list)
    line.add_yaxis(series_name = '专辑',y_axis = album_list)

    line.set_global_opts(
        #设置图例形状
        legend_opts=opts.LegendOpts(legend_icon='pin'),
        #设置图表主标题，副标题和标题位置
        title_opts=opts.TitleOpts(title = '我喜欢的九位歌手',subtitle='数错了,是十位',pos_left='20%'),
        #添加坐标轴名称，位置以及大小，name_gap表示名称与x轴距离，font_size是字体大小
        xaxis_opts = opts.AxisOpts(name = '歌手',name_location='center',name_gap=25,name_textstyle_opts=opts.TextStyleOpts(font_size = 20)),
        yaxis_opts = opts.AxisOpts(name = '单曲数量/首'),
        datazoom_opts = opts.DataZoomOpts(range_start=10,range_end=30), # 坐标轴进行缩放
        
        )

    return line

line = set_line()
line.render('折线图2.html')

