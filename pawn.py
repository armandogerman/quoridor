from tkinter import NW


def position(i):
  for j in range(17):
    col = i-(j*34)
    acu=0
    if col<=17:
      while col>=0:
        if col==0:
          return j,acu
        elif col>0:
          col-=2
          acu+=1
# def index(j,col):
#     return j*17+col

def pawnmovedown(request_data,pc):
    s=request_data['data']['side']
    if pc+17<288:   # 1
        if request_data['data']['board'][pc+17]=='-' or request_data['data']['board'][pc+17]=='*' or request_data['data']['board'][pc+17]=='|':
            return None
    if pc+51<288: # 2
        if request_data['data']['board'][pc+51]=='-' or request_data['data']['board'][pc+51]=='*' or request_data['data']['board'][pc+51]=='|':
            return None  
    if pc+34<288: # 3 4 y 5 
        if request_data['data']['board'][pc+34]==' ':
            return position(pc), position(pc+34)
        elif request_data['data']['board'][pc+34]!=s:
            if pc+68<288:
                if request_data['data']['board'][pc+68]==' ':
                    return position(pc), position(pc+68)
            if pc+36<288:
                if request_data['data']['board'][pc+36]==' ':
                    a=position(pc)
                    b=position(pc+36)
                    if a[1]==b[1]+1 or a[1]==b[1]-1:
                        return a, b    #5.r)
            if pc+32<288:               
                if request_data['data']['board'][pc+32]==' ':
                    a=position(pc)
                    b=position(pc+32)
                    if a[1]==b[1]+1 or a[1]==b[1]-1:
                        return a, b    #5.l)


def pawnmoveleft(request_data,pc):
    if request_data['data']['board'][pc] == request_data['data']['side']:
        if request_data['data']['board'][pc+1] != '|': 
            if request_data['data']['board'][pc-2] == ' ':
                if request_data['data']['side']=='S':
                    if request_data['data']['board'][pc-19]==' ':
                        return position(pc), position(pc-2)
                elif request_data['data']['side']=='N':
                    if request_data['data']['board'][pc+19]==' ':
                        return position(pc), position(pc-2)

def pawnmoveright(request_data,pc):
    if request_data['data']['board'][pc] == request_data['data']['side']:
        if request_data['data']['board'][pc+1] != '|': 
            if request_data['data']['board'][pc+2] == ' ':
                if request_data['data']['side']=='S':
                    if request_data['data']['board'][pc-15]==' ':
                        return position(pc), position(pc+2)
                elif request_data['data']['side']=='N':
                    if request_data['data']['board'][pc+15]==' ':
                        return position(pc), position(pc+2)

def pawnmoveup(request_data,pc):
    if request_data['data']['board'][pc-17] == '-'and pc>=17:
        return None
    elif request_data['data']['board'][pc-34] == ' 'and pc>=34:
        return position(pc), position(pc-34)
    elif request_data['data']['board'][pc-34] != request_data['data']['side'] and pc>=34:
        if request_data['data']['board'][pc-68] == ' ' and pc>=68:
            return position(pc), position(pc-68)
        elif pc<=50 and request_data['data']['board'][pc-36] == ' ' and  pc-36>=0:
            return position(pc), position(pc-36)
        elif pc<=50 and request_data['data']['board'][pc-32] == ' ' and  pc-32>=0:
            return position(pc), position(pc-32)

def movepc(request_data,pc):
    if request_data['data']['side']=="N":
        if pawnmovedown(request_data,pc) != None:
            print("pawnmovedown N",pawnmovedown(request_data,pc))
            return pawnmovedown(request_data,pc)
        elif pawnmoveleft(request_data,pc) != None:
            print("pawnmoveleft N",pawnmoveleft(request_data,pc))
            return pawnmoveleft(request_data,pc)
        elif pawnmoveright(request_data,pc) != None:
            print("pawnmoveright N",pawnmoveright(request_data,pc))
            return pawnmoveright(request_data,pc)
        elif pawnmoveup(request_data,pc) !=None:
            print("pawnmoveup N",pawnmoveup(request_data,pc))
            return pawnmoveup(request_data,pc)
    if request_data['data']['side']=="S":
        if pawnmoveup(request_data,pc) !=None:
            print("pawnmoveup S",pawnmoveup(request_data,pc))
            return pawnmoveup(request_data,pc)
        elif pawnmoveleft(request_data,pc) != None:
            print("pawnmoveleft S",pawnmoveleft(request_data,pc))
            return pawnmoveleft(request_data,pc)
        elif pawnmoveright(request_data,pc) != None:
            print("pawnmoveright",pawnmoveright(request_data,pc))
            return pawnmoveright(request_data,pc)
        elif pawnmoveup(request_data,pc) !=None:
            print("pawnmoveup S",pawnmoveup(request_data,pc))
            return pawnmoveup(request_data,pc)
        elif pawnmovedown(request_data,pc) != None:
            print("pawnmovedown S",pawnmovedown(request_data,pc))
            return pawnmovedown(request_data,pc)

# for i in range(17):
#     for j in range(17):
#         print("index",index(i,j),"i",i,"j",j)

# request_data={"event": "your_turn", "data": {"side": "N", "score_2": 5517.0, "board": "  N N              -*-              S                      -*-          S     S N                -*-                                                           -*-                                                                                                 -*-                           ", "player_1": "armandogerman@hotmail.com", "score_1": 8654.0, "walls": 10.0, "player_2": "mamerida2013@gmail.com", "remaining_moves": 66.0, "turn_token": "166bc6a3-8982-414c-ae97-51d2d9b742f8", "game_id": "5243783e-dc43-11ec-aef0-7ecdf393f9cc"}}
# print(pawnmovedown(request_data,80))
