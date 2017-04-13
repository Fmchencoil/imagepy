# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:35:09 2016

@author: yxl
"""
from core.engines import Tool

class Plugin(Tool):
    title = 'Scope'
    def __init__(self):
        self.ox, self.oy = 0, 0
            
    def mouse_down(self, ips, x, y, btn, **key):
        if btn==2:
            self.ox, self.oy = key['canvas'].to_panel_coor(x,y)
            print self.ox, self.oy
        #print 'down', self.ox, self.oy
        if btn==1: key['canvas'].zoomout(x,y)
        if btn==3: key['canvas'].zoomin(x,y)
    
    def mouse_up(self, ips, x, y, btn, **key):
        pass
    
    def mouse_move(self, ips, x, y, btn, **key):
        if btn==2:
            x,y = key['canvas'].to_panel_coor(x,y)
            #print 'x,y',x,y
            #print 'dx,dy:', x-self.ox, y-self.oy
            key['canvas'].move(x-self.ox, y-self.oy)
        self.ox, self.oy = x,y
        
    def mouse_wheel(self, ips, x, y, d, **key):
        if d>0:key['canvas'].zoomout(x,y)
        if d<0:key['canvas'].zoomin(x,y)