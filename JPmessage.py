# -*- coding: utf-8 -*-
"""

Windows と Mac の両方で日本語フォントを指定して日本語メッセージを表示させる．

@author: Hitoshi HABE (habe@kindai.ac.jp)
"""

import numpy as np
import matplotlib.pyplot as pl
import platform
from matplotlib import font_manager

# 日本語フォントの設定（はじまり）
# Windows と Mac のどちらで動かしているのかを判断して日本語フォントに指定を切り替える
systemname=platform.system()
if systemname == 'Windows':       
    font_path = 'C:\\Windows\\Fonts\\msgothic.ttc'
    font_prop = font_manager.FontProperties(fname=font_path)
    font_prop.set_style('normal')
    font_prop.set_weight('light')
    font_prop.set_size('12')
elif systemname == 'Darwin':       
    font_path = '/Library/Fonts/Osaka.ttf'
    font_prop = font_manager.FontProperties(fname=font_path)
    font_prop.set_style('normal')
    font_prop.set_weight('light')
    font_prop.set_size('12')
# 日本語フォントの設定 （おわり）

# サンプルとして適当に sin 関数のグラフを表示してみる．
x_min=-1
x_max=1
x_step=0.05    
x=np.r_[x_min:x_max:x_step]
y=np.sin((2*np.pi)*x)

title=u'サインカーブをプロットした結果'
xlabel=u'xの値'
ylabel=u'yの値'

pl.plot(x,y.real,'r-',marker=None)
pl.title(title,fontproperties=font_prop)
pl.xlabel(xlabel,fontproperties=font_prop)
pl.ylabel(ylabel,fontproperties=font_prop)
pl.show()
