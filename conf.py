# -*- coding:utf-8 -*-  
import pygame
from pygame.locals import *
class GlobalVar: 
    #黑子还是白子先下   hei:黑(AI)   bai:白
    hei_bai = 'hei'
    #AI对人
    useAI = True
    #AI对AI
    AI_AI = False
    
    AI_WIN_COUNT = 0
    YOU_WIN_COUNT = 0
#允许点击的误差，离远点多远算正常点击
wc = 10
#初始化棋盘位置
myList = [([0] * 15) for i in range(15)]
#棋盘左上角棋子的位置
x1,y1=167,65
#初始化所有棋子的位置
for i in range(15):
    for j in range(15):
        myList[i][j]=[x1,y1,'']
        x1 = x1 + 25
    x1 = 167
    y1 = y1 + 25
#根据用户点击的位置获取棋子的准确位置并记录
def getXY(x, y):
    for list_len in range(len(myList)):
        _y = myList[list_len][0][1]
        if _y>(y-wc) and _y<(y+wc):
            for list2_len in range(len(myList[list_len])):
                _x = myList[list_len][list2_len][0]
                if _x>(x-wc) and _x<(x+wc):
                    if myList[list_len][list2_len][2]!='':#如果这个位置上已经有子，则无效
                        return 0
                    return (_x,myList[list_len][list2_len][1],list_len,list2_len)
    return 0

#判断这个坐标上是否有当前颜色的子
def isok(list_len, list2_len):
    if(list_len<0 or list2_len<0 or list_len>14 or list2_len>14):
        return False
    if myList[list_len][list2_len][2]==GlobalVar.hei_bai:
        return True
    return False

#检查是否获胜,list_len，list2_len 坐标对应的数组下标
def cheak_win(list_len,list2_len):
    #print("cheak_win:",list_len,list2_len)
    #在一横行上获胜
    for i in range(5):
        a = isok(list_len,list2_len-4+i)
        b = isok(list_len,list2_len-3+i)
        c = isok(list_len,list2_len-2+i)
        d = isok(list_len,list2_len-1+i)
        e = isok(list_len,list2_len+i)
        if a and b and c and d and e:
            #print("..................",GlobalVar.hei_bai,"赢了")
            return True
    #在一竖行上获胜
    for i in range(5):
        a = isok(list_len-4+i,list2_len)
        b = isok(list_len-3+i,list2_len)
        c = isok(list_len-2+i,list2_len)
        d = isok(list_len-1+i,list2_len)
        e = isok(list_len+i,list2_len)
        if a and b and c and d and e:
            #print("..................",GlobalVar.hei_bai,"赢了")
            return True
    #在一斜行上获胜（左上-》右下）
    for i in range(5):
        a = isok(list_len-4+i,list2_len-4+i)
        b = isok(list_len-3+i,list2_len-3+i)
        c = isok(list_len-2+i,list2_len-2+i)
        d = isok(list_len-1+i,list2_len-1+i)
        e = isok(list_len+i,list2_len+i)
        if a and b and c and d and e:
            #print("..................",GlobalVar.hei_bai,"赢了")
            return True
    #在一斜行上获胜（左下-》右上）
    for i in range(5):
        a = isok(list_len+4-i,list2_len-4+i)
        b = isok(list_len+3-i,list2_len-3+i)
        c = isok(list_len+2-i,list2_len-2+i)
        d = isok(list_len+1-i,list2_len-1+i)
        e = isok(list_len-i,list2_len+i)
        if a and b and c and d and e:
            #print("..................",GlobalVar.hei_bai,"赢了")
            return True
    return False
def show_text(surface_handle, pos, text, color, font_bold = False, font_size = 13, font_italic = False):   
    #获取系统字体，并设置文字大小  
    cur_font = pygame.font.SysFont("SimHei", font_size)  
    #设置是否加粗属性  
    cur_font.set_bold(font_bold)  
    #设置是否斜体属性  
    cur_font.set_italic(font_italic)  
    #设置文字内容  
    text_fmt = cur_font.render(text, 1, color)  
    #绘制文字  
    surface_handle.blit(text_fmt, pos) 