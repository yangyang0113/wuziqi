# -*- coding:utf-8 -*-  
import pygame
from pygame.locals import *
from wuziqi.conf import *
from wuziqi.ai1 import *
import time
#背景图片
background_image_filename = 'img/bg.jpg'
background_image_filename2 = 'img/bg.png'
hei_image_filename = 'img/hei.png'
bai_image_filename = 'img/bai.png'
myicon = 'img/icon.png'
pygame.init()
screen = pygame.display.set_mode((800, 528), 0, 32)
background = pygame.image.load(background_image_filename).convert()
background2 = pygame.image.load(background_image_filename2).convert()
icon2 = pygame.image.load(myicon).convert_alpha()
hei = pygame.image.load(hei_image_filename).convert_alpha()
bai = pygame.image.load(bai_image_filename).convert_alpha()
pygame.display.set_icon(icon2)
pygame.display.set_caption("流血五子棋 v1.0             按F1重新开始!!!")
x2,y2=0,0
screen.fill((0,0,0))
screen.blit(background, (150,50))
screen.blit(background2, (550,50))

def change_show():
    screen.blit(background2, (550,50))
    title_info = "win_count"
    show_text(screen, (570, 50), title_info, (255, 255, 255), False, 20)
    title_info = "AI     " +str(GlobalVar.AI_WIN_COUNT)
    show_text(screen, (570, 100), title_info, (255, 255, 255), False, 20)
    title_info = "YOU    "  +str(GlobalVar.YOU_WIN_COUNT)
    show_text(screen, (570, 150), title_info, (255, 255, 255), False, 20)
change_show()
while True:
    for event in pygame.event.get():
        global hei_bai
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            #f1  重新开始
            if event.key == K_F1:
                #棋盘刷新，参数重置
                screen.blit(background, (150,50))
                GlobalVar.AI_WIN_COUNT = 0
                GlobalVar.YOU_WIN_COUNT = 0
                change_show()
                for a in myList:
                    for b in a:
                        b[2]=''
        if event.type == 6:
            #放开鼠标,获取鼠标坐标
            x, y = pygame.mouse.get_pos()
            #根据用户点击的位置，查找棋盘对应的点
            xy = getXY(x-10,y-10)
            if(xy!=0):
                x2 = xy[0]
                y2 = xy[1]
                myList[xy[2]][xy[3]][2] = GlobalVar.hei_bai #将黑子或者白字标记到棋盘
                iswin = cheak_win(xy[2],xy[3])#检查是否赢棋
                if iswin:
                    GlobalVar.YOU_WIN_COUNT = GlobalVar.YOU_WIN_COUNT + 1
                    change_show()
    #计算出新的坐标
    if(x2!=0):
        if(GlobalVar.useAI==False or (GlobalVar.useAI==True and GlobalVar.hei_bai=='bai')):
            if(GlobalVar.hei_bai=='bai'):
                screen.blit(bai, (x2,y2))
            if(GlobalVar.hei_bai=='hei'):
                screen.blit(hei, (x2,y2))
            #print(GlobalVar.hei_bai,"方下子完毕")
        x2 = 0
        if(GlobalVar.hei_bai=='bai'):
            GlobalVar.hei_bai='hei'
        else:
            GlobalVar.hei_bai='bai'
    if(GlobalVar.useAI==True and GlobalVar.hei_bai=="hei"):
        #print("AI下子完毕hei")
        aixy = ai1.getAIXY()#这里是ai接口#
        if(aixy!=0):
            myList[aixy[2]][aixy[3]][2] = GlobalVar.hei_bai#将黑子或者白字标记到棋盘
            screen.blit(hei,(aixy[0],aixy[1]))
            iswin = cheak_win(aixy[2],aixy[3])#检查是否赢棋
            if iswin:
                GlobalVar.AI_WIN_COUNT = GlobalVar.AI_WIN_COUNT + 1
                change_show()
            GlobalVar.hei_bai="bai"
    #刷新图形界面
    pygame.display.update()
    '''AI博弈'''
    if GlobalVar.AI_AI==True:
        #time.sleep(0.1)
        if(GlobalVar.useAI==True and GlobalVar.hei_bai=="bai"):
            #print("AI下子完毕bai")
            aixy = ai1.getAIXY()#这里是ai接口#
            if(aixy!=0):
                myList[aixy[2]][aixy[3]][2] = GlobalVar.hei_bai#将黑子或者白字标记到棋盘
                screen.blit(bai,(aixy[0],aixy[1]))
                cheak_win(aixy[2],aixy[3])#检查是否赢棋
                GlobalVar.hei_bai="hei"
        pygame.display.update()
        #time.sleep(0.1)
    
