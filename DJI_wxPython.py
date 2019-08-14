# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:51:41 2019

wxPython plot

@author: pNser copy Dazhuang @NJU
"""

import datetime as dt
import myfinance as finance
import matplotlib.pyplot as plt
import pandas as pd
import _thread as thread
import wx

#不明白这行的目的
ID_EVENT_REFRESH = 9999

#定义一个wx.Frame的子类
class StockFrame(wx.Frame):
    
    #定义选择框的初始状态
    option_list = {'open':True,'close':True,'high':False,'low':False,'volume':False}
    
    def __init__(self,title):
        
        wx.Frame.__init__(self,None,title=title,size=(430,600))
        
        #创建状态栏
        self.CreateStatusBar()
        
        #创建菜单栏,菜单栏文字
        menuBar = wx.MenuBar()
        filemenu = wx.Menu()
        menuBar.Append(filemenu,"&File")
        #增加“Refresh”菜单以及在状态栏说明文字，绑定方法
        menuRefresh = filemenu.Append(ID_EVENT_REFRESH,"&Refresh","Refresh the price")
        self.Bind(wx.EVT_MENU,self.OnRefresh,menuRefresh)
        #增加“Quit”菜单以及在状态栏说明文字，绑定方法
        menuQuit = filemenu.Append(wx.ID_EXIT,"&Quit","Terminate the program")
        self.Bind(wx.EVT_MENU,self.OnQuit,menuQuit)
        #菜单栏子项设置完成后完成菜单栏设定
        self.SetMenuBar(menuBar)        
        
        #创建panel 
        panel = wx.Panel(self)
        
        #创建股票代码（code）文本框sizer,水平放置
        codeSizer = wx.BoxSizer(wx.HORIZONTAL)
        #静态文字标签，在codesizer中加入标签位置下对齐
        labelText = wx.StaticText(panel,label="Stock Code:")
        codeSizer.Add(labelText,0,wx.ALIGN_BOTTOM)
        #TODO: need a better way yo put a spacer here than this:
        #codeSizer.Add((10,10))
        #文本框，初始值“BA”，出发回车键响应
        codeText = wx.TextCtrl(panel,value="BA",style=wx.TE_PROCESS_ENTER)
        #绑定回车键方法到Event上
        self.Bind(wx.EVT_TEXT_ENTER,self.OnTextSubmitted,codeText)
        #codesizer中增加文本框位置
        codeSizer.Add(codeText)
        
        #创建optionsizer，水平放置
        optionSizer = wx.BoxSizer(wx.HORIZONTAL)
        #增加check event的方法，并在optionsizer中增加checkbox位置
        for key, value in self.option_list.items():
            checkBox = wx.CheckBox(panel,label=key.title())
            checkBox.SetValue(value)
            self.Bind(wx.EVT_CHECKBOX,self.OnChecked)
            optionSizer.Add(checkBox)
        
        #增加列表,report类型
        self.list = wx.ListCtrl(panel,wx.NewId(),style=wx.LC_REPORT)
        #执行createHeaer程序
        self.createHeader()
        
        #增加list显示内容，对列表内双击事件绑定方法
        pos = self.list.InsertItem(0,"__")
        self.list.SetItem(pos,1,"loading...")
        self.list.SetItem(pos,2,"__")
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED,self.OnDoubleClick,self.list)
        
        #增加ctrlsizer
        ctrlSizer = wx.BoxSizer(wx.HORIZONTAL)
        ctrlSizer.Add((10,10))
        
        #增加退出按钮及刷新按钮，分别绑定方法及放置位置
        buttonQuit = wx.Button(panel,-1,"Quit")
        self.Bind(wx.EVT_BUTTON,self.OnQuit,buttonQuit)
        ctrlSizer.Add(buttonQuit,1)
        buttonRefresh = wx.Button(panel,-1,"Refresh")
        self.Bind(wx.EVT_BUTTON,self.OnRefresh,buttonRefresh)
        ctrlSizer.Add(buttonRefresh,1,wx.LEFT|wx.BOTTOM)
        
        #设置一个总的sizer，垂直方式，然后将其他子sizer放入
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(codeSizer,0,wx.ALL,5)
        sizer.Add(optionSizer,0,wx.ALL,5)
        sizer.Add(self.list,-1,wx.ALL | wx.EXPAND,5)
        sizer.Add(ctrlSizer,0,wx.ALIGN_BOTTOM)
        
        #最终整理sizer
        panel.SetSizerAndFit(sizer)
        self.Center()
        
        #start to load data right after the window omes up
        self.OnRefresh(None)
    
    #创建list表头    
    def createHeader(self):
        self.list.InsertColumn(0,"Symbol")
        self.list.InsertColumn(1,"Name")
        self.list.InsertColumn(2,"Last Trade")

    #list里面增加数据        
    def setData(self,data):
        self.list.ClearAll()
        self.createHeader()
        pos = 0
        for row in data:
            pos = self.list.InsertItem(pos+1,row['code'])
            self.list.SetItem(pos,1,row['name'])
            self.list.SetColumnWidth(1,-1)
            self.list.SetItem(pos,2,str(row['price']))
            if pos%2 == 0:
                #set new look and feel for odd lines
                self.list.SetItemBackgroundColour(pos,(134,225,249))
    
    #画图            
    def PlotData(self,code):
        quotes = finance.get_quotes_historical(code)
        fields = ['date','open','close','high','low','volume']
        dates = []
        for i in range(0,len(quotes)):
            x = dt.datetime.utcfromtimestamp(int(quotes[i]['date']))
            y = dt.datetime.strftime(x,'%Y-%m-%d')
            dates.append(y)
        quotesdf = pd.DataFrame(quotes,index=dates,columns=fields)
        
        #remove unchecked fileds
        fileds_to_drop = ['date']
        for key, value in self.option_list.items():
            if not value:
                fileds_to_drop.append(key)
                
        quotesdf = quotesdf.drop(fileds_to_drop,axis=1)
        quotesdf.plot()
        plt.show()
    
    #响应列表双击方法    
    def OnDoubleClick(self,event):
        self.PlotData(event.GetText())
    
    #响应文本框输入回车方法    
    def OnTextSubmitted(self,event):
        self.PlotData(event.GetString())
    
    #获取复选框数据
    def OnChecked(self,event):
        checkBox = event.GetEventObject()
        text = checkBox.GetLabel().lower()
        self.option_list[text] = checkBox.GetValue()
    
    #响应退出按钮/菜单方法    
    def OnQuit(self,event):
        self.Close()
        self.Destroy()
        
    #响应刷新按钮/菜单方法    
    def OnRefresh(self,event):
        thread.start_new_thread(self.retrieve_quotes,())

    #获取 DJI数据
    def retrieve_quotes(self):
        data = finance.get_dji_list()
        if data:
            self.setData(data)
        else:
            wx.MessageBox('Download failed.','Message', wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App(False)
    #创建StockFrame实例，名称为"Dow Jons Industrial Average(^DJI)"
    top = StockFrame("Dow Jons Industrial Average(^DJI)")
    top.Show(True)
    app.MainLoop()            
        
        
        