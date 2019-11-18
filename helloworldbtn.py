# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 16:36:50 2019

@author: pNser copy Dazhuang@NJU
"""

# Filename: helloworldbtn.py
import wx 
 
class Frame1(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title)
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text1 = wx.TextCtrl(panel, value = "Hello, World!",
                    size = (200,280), style = wx.TE_MULTILINE)
        sizer.Add(self.text1, 0, wx.ALIGN_TOP | wx.EXPAND)
        button = wx.Button(panel, label = "Click Me")
        sizer.Add(button)
        panel.SetSizerAndFit(sizer)        
        panel.Layout()
        self.Bind(wx.EVT_BUTTON,self.OnClick,button)
        self.Show(True)
    def OnClick(self, text):
        self.text1.AppendText("\nHello, World!")
         
if __name__ == '__main__': 
        app = wx.App()
        frame = Frame1(None, "Hello World in wxPython")
        app.MainLoop()
