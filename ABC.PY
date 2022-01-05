#!/usr/bin/env python3                             告诉操作系统这是一个Python函数，WINDOWS忽略这条
# -*- coding: utf-8 -*-                            使用utf-8编码
#Author sonlee qian
from base64 import decode
import os ,random
import sys
import time
import multiprocessing
from threading import Thread  
import tkinter as tk  # 使用Tkinter前需要先导入




bidding_quotation_list = [100, 102, 105, 110, 111, 109, 120, 90, 85, 112 , 103, 122, 119 , 88, 83 , 119 , 119.2 ,119.3 , 119.4 , 119.5 , 115.1 , 115.2, 115.3 , 115.4 , 115.3 , 115.2 ,115.1, 115, 114.9,114.8,114.7]      #投标人报价列表
float_down_delta = 0.06      #下浮率delta
maximum_bid_limit = 120      #最高投标限价
minimum_bid_limit = 80       #最低投标限价
K = 0.98                     #下浮系数K

def getA() ->float: 
    A = maximum_bid_limit*(1-float_down_delta)
   
    return A

def get_between(list1 , thestandard , min_percent , max_percent ) ->list:      ##定义一个函数获取区间值
    temp_list = []
    for i in range(len(list1)):
          if list1[i] < max_percent * thestandard and bidding_quotation_list[i] >= min_percent * thestandard :
                temp_list.append(list1[i])
          else: pass
    return temp_list
      
      
      
def getB() ->float:
    
    list_0_89 = get_between ( bidding_quotation_list , getA() , 0 , 0.89 )
    list_89_92 = get_between ( bidding_quotation_list , getA() , 0.89 , 0.92 )
    list_92_95 = get_between ( bidding_quotation_list , getA() , 0.92 , 0.95 )
    
    
    ##    若在A值的95%-92% （含）、 92%-89% （含）范围内，则在两个区间内各抽取一个评标价
    if  len(list_89_92) and len(list_92_95) : 
      rand_89_92 = list_89_92[random.randint(0,len(list_89_92) - 1)]
      rand_92_95 = list_89_92[random.randint(0,len(list_92_95) - 1)]
      list_0_89.append(rand_89_92)
      list_0_89.append(rand_92_95)
      
      B = list_0_89[random.randint(0,len(list_0_89) - 1)]
     
      return B
       
    else :
      B = bidding_quotation_list[random.randint(0,len(bidding_quotation_list) - 1)]
      return B
     
    
def getC() -> float :                          ##C=在规定范围内的最低评标价；
  C = min(bidding_quotation_list)
  return  C
    
def getBasePrice () -> float:               ##评标基准价=（A×50%+B×30%+C×20%）×K
  BasePrice = getA()*0.5 + getB()*0.3 + getC()*0.2
  BasePrice = BasePrice * K
  return BasePrice
  
if __name__ == '__main__':
      
  print('A=', getA())
  print('B=', getB())
  print('C=', getC())  
  print('BasePrice=', getBasePrice ())
  



  ##  *****************************以下为窗口代码区域，使用Tkinter建立图形界面******************************************


  # 第1步，实例化object，建立窗口window
  window = tk.Tk()
 

 # 第2步，给窗口的可视化起名字
  window.title('ABC合成法')
 

 # 第3步，设定窗口的大小(长 * 宽)
  window.geometry('700x300')  # 这里的乘是小x
 

 # 第4步，在图形界面上设定标签
  l0 = tk.Label(window, text='ABC合成法计算值：', bg='green', font=('Arial', 12), width=30, height=2)
 # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
 

 # 第5步，放置标签
  l0.pack()    # Label内容content区域放置位置，自动调节尺寸
 # 放置lable的方法有：1）l.pack(); 2)l.place();
 

  var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
  l1 = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
  # 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
  l1.pack()
 
 
 



  e1 = tk.Entry(window, show=None, font=('Arial', 14))   # 显示成密文形式
  e2 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
  e1.pack()
  e2.pack()

 # 第5步，在窗口界面设置放置Button按键
  on_hit = False

  def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set(str(getBasePrice ()))
    else:
        on_hit = False
        var.set('')
 
  b = tk.Button(window, text='RUN', font=('Arial', 12), width=10, height=1, command=hit_me)
  b.pack()
  
  t = tk.Text(window, height=5)  ##多行文本窗口
  t.pack()

 #主窗口循环显示
  window.mainloop()
 # 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
 # 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。


