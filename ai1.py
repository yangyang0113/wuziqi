import random
from wuziqi.conf import myList, cheak_win, GlobalVar
class temp:
    listlen = 0
    list2len = 0
    heibai = ''
    
def changeHeiBai():
    if GlobalVar.hei_bai=='hei':
        return 'bai'
    else:
        return 'hei'
#判断这个坐标上是否有当前颜色的子
def aiisok(list_len, list2_len):
    if list_len==temp.listlen and list2_len==temp.list2len:
        return True
    if(list_len<0 or list2_len<0 or list_len>14 or list2_len>14):
        return False
    if myList[list_len][list2_len][2]==temp.heibai:
        return True
    return False

#检查是否获胜,list_len，list2_len 坐标对应的数组下标
def aicheak_win1(list_len,list2_len):
    temp.listlen = list_len
    temp.list2len = list2_len
    #在一横行上形成5子
    for i in range(5):
        a = aiisok(list_len,list2_len-4+i)
        b = aiisok(list_len,list2_len-3+i)
        c = aiisok(list_len,list2_len-2+i)
        d = aiisok(list_len,list2_len-1+i)
        e = aiisok(list_len,list2_len+i)
        if a and b and c and d and e:
            return True
    #在一竖行上形成5子
    for i in range(5):
        a = aiisok(list_len-4+i,list2_len)
        b = aiisok(list_len-3+i,list2_len)
        c = aiisok(list_len-2+i,list2_len)
        d = aiisok(list_len-1+i,list2_len)
        e = aiisok(list_len+i,list2_len)
        if a and b and c and d and e:
            return True
    #在一斜行上形成5子（左上-》右下）
    for i in range(5):
        a = aiisok(list_len-4+i,list2_len-4+i)
        b = aiisok(list_len-3+i,list2_len-3+i)
        c = aiisok(list_len-2+i,list2_len-2+i)
        d = aiisok(list_len-1+i,list2_len-1+i)
        e = aiisok(list_len+i,list2_len+i)
        if a and b and c and d and e:
            return True
    #在一斜行上形成5子（左下-》右上）
    for i in range(5):
        a = aiisok(list_len+4-i,list2_len-4+i)
        b = aiisok(list_len+3-i,list2_len-3+i)
        c = aiisok(list_len+2-i,list2_len-2+i)
        d = aiisok(list_len+1-i,list2_len-1+i)
        e = aiisok(list_len-i,list2_len+i)
        if a and b and c and d and e:
            return True
def aicheak_win2(list_len,list2_len):
    temp.listlen = list_len
    temp.list2len = list2_len
    #在一横行上形成4子
    for i in range(4):
        b = aiisok(list_len,list2_len-3+i)
        c = aiisok(list_len,list2_len-2+i)
        d = aiisok(list_len,list2_len-1+i)
        e = aiisok(list_len,list2_len+i)
        if b and c and d and e:
            return True
    #在一竖行上形成4子
    for i in range(4):
        b = aiisok(list_len-3+i,list2_len)
        c = aiisok(list_len-2+i,list2_len)
        d = aiisok(list_len-1+i,list2_len)
        e = aiisok(list_len+i,list2_len)
        if b and c and d and e:
            return True
    #在一斜行上形成4子（左上-》右下）
    for i in range(4):
        b = aiisok(list_len-3+i,list2_len-3+i)
        c = aiisok(list_len-2+i,list2_len-2+i)
        d = aiisok(list_len-1+i,list2_len-1+i)
        e = aiisok(list_len+i,list2_len+i)
        if b and c and d and e:
            return True
    #在一斜行上形成4子（左下-》右上）
    for i in range(4):
        b = aiisok(list_len+3-i,list2_len-3+i)
        c = aiisok(list_len+2-i,list2_len-2+i)
        d = aiisok(list_len+1-i,list2_len-1+i)
        e = aiisok(list_len-i,list2_len+i)
        if b and c and d and e:
            return True
def aicheak_win3(list_len,list2_len):
    temp.listlen = list_len
    temp.list2len = list2_len
    #在一横行上形成3子
    for i in range(3):
        c = aiisok(list_len,list2_len-2+i)
        d = aiisok(list_len,list2_len-1+i)
        e = aiisok(list_len,list2_len+i)
        if c and d and e:
            return True
    #在一竖行上形成3子
    for i in range(3):
        c = aiisok(list_len-2+i,list2_len)
        d = aiisok(list_len-1+i,list2_len)
        e = aiisok(list_len+i,list2_len)
        if c and d and e:
            return True
    #在一斜行上形成3子（左上-》右下）
    for i in range(3):
        c = aiisok(list_len-2+i,list2_len-2+i)
        d = aiisok(list_len-1+i,list2_len-1+i)
        e = aiisok(list_len+i,list2_len+i)
        if c and d and e:
            return True
    #在一斜行上形成3子（左下-》右上）
    for i in range(3):
        c = aiisok(list_len+2-i,list2_len-2+i)
        d = aiisok(list_len+1-i,list2_len-1+i)
        e = aiisok(list_len-i,list2_len+i)
        if c and d and e:
            return True

def aicheak_win4(list_len,list2_len):
    temp.listlen = list_len
    temp.list2len = list2_len
    #在一横行上形成2子
    for i in range(2):
        d = aiisok(list_len,list2_len-1+i)
        e = aiisok(list_len,list2_len+i)
        if d and e:
            return True
    #在一竖行上形成2子
    for i in range(2):
        d = aiisok(list_len-1+i,list2_len)
        e = aiisok(list_len+i,list2_len)
        if d and e:
            return True
    #在一斜行上形成2子（左上-》右下）
    for i in range(2):
        d = aiisok(list_len-1+i,list2_len-1+i)
        e = aiisok(list_len+i,list2_len+i)
        if d and e:
            return True
    #在一斜行上形成2子（左下-》右上）
    for i in range(2):
        d = aiisok(list_len+1-i,list2_len-1+i)
        e = aiisok(list_len-i,list2_len+i)
        if d and e:
            return True
#先去redis查询，如果有结果直接返回，后面做机器学习会用到
def getRedis():
    return False
#权重（参数，1：考虑自己，2：考虑对手）
#权重1 做5连子
def getWeight1(num):
    temp.heibai=GlobalVar.hei_bai
    if num ==2:
        temp.heibai = changeHeiBai()
    for list_len in range(len(myList)):
            for list2_len in range(len(myList[list_len])):
                if myList[list_len][list2_len][2]=='':
                    if(aicheak_win1(list_len,list2_len)):
                        return (myList[list_len][list2_len][0],myList[list_len][list2_len][1],list_len,list2_len)
    return False
#权重2 做4连子
def getWeight2(num):
    temp.heibai=GlobalVar.hei_bai
    if num ==2:
        temp.heibai = changeHeiBai()
    for list_len in range(len(myList)):
            for list2_len in range(len(myList[list_len])):
                if myList[list_len][list2_len][2]=='':
                    if(aicheak_win2(list_len,list2_len)):
                        return (myList[list_len][list2_len][0],myList[list_len][list2_len][1],list_len,list2_len)
    return False
#权重3 做3连子
def getWeight3(num):
    temp.heibai=GlobalVar.hei_bai
    if num ==2:
        temp.heibai = changeHeiBai()
    for list_len in range(len(myList)):
            for list2_len in range(len(myList[list_len])):
                if myList[list_len][list2_len][2]=='':
                    if(aicheak_win3(list_len,list2_len)):
                        return (myList[list_len][list2_len][0],myList[list_len][list2_len][1],list_len,list2_len)
    return False
#权重4 做2连子
def getWeight4(num):
    temp.heibai=GlobalVar.hei_bai
    if num ==2:
        temp.heibai = changeHeiBai()
    for list_len in range(len(myList)):
            for list2_len in range(len(myList[list_len])):
                if myList[list_len][list2_len][2]=='':
                    if(aicheak_win4(list_len,list2_len)):
                        return (myList[list_len][list2_len][0],myList[list_len][list2_len][1],list_len,list2_len)
    return False
  
        
class ai1:
    #ai下子，并记录到棋盘,返回棋盘坐标与数组下标
    def getAIXY():  # @NoSelf
        re = getRedis()
        if re!=False:
            return re
        re = getWeight1(1)
        if re!=False:
            return re
        re = getWeight1(2)
        if re!=False:
            return re
        re = getWeight2(1)
        if re!=False:
            return re
        re = getWeight2(2)
        if re!=False:
            return re
        re = getWeight3(1)
        if re!=False:
            return re
        re = getWeight3(2)
        if re!=False:
            return re
        re = getWeight4(1)
        if re!=False:
            return re
        re = getWeight4(2)
        if re!=False:
            return re
        #如果正中间没有子，那就下正中间
        if myList[7][7][2]=="":
            return (myList[7][7][0],myList[7][7][1],7,7)
        #ai找不到，那就随便找个地方下子吧
        for list_len in range(len(myList)):
            for list2_len in range(len(myList[list_len])):
                li = myList[list_len][list2_len]
                if li[2]=='':
                    return (li[0],li[1],list_len,list2_len)
        #随便找地方都找不到，那就说明棋盘下满了。。。游戏结束
        return 0
