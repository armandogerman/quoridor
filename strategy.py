from pawn import *
from wall import *

def distance(request_data,pcs):
    if request_data['data']['side']=="N":
        acu=0
        while pcs<=254:
            if walldown(request_data,pcs)==1:
                acu+=1
            elif walldown(request_data,pcs)==2:
                acu+=2
            elif walldown(request_data,pcs)==3:
                acu+=6
            elif walldown(request_data,pcs)==4:
                acu+=8
            pcs=pcs+34
        return acu
    if request_data['data']['side']=="S":
        acu=0
        while pcs>34:
            if wallup(request_data,pcs)==1:
                acu+=1
            elif wallup(request_data,pcs)==2:
                acu+=2
            elif wallup(request_data,pcs)==3:
                acu+=6
            elif wallup(request_data,pcs)==4:
                acu+=8
            pcs=pcs-34
        return acu
def prt(request_data):
    board=request_data['data']['board']
    p2=request_data['data']['player_2']
    sc2=request_data['data']['score_2']
    side=request_data['data']['side']
    rem=int(request_data['data']['remaining_moves'])
    turn_token=request_data['data']['turn_token']
    game_id=request_data['data']['game_id']
    p1=request_data['data']['player_1']
    sc1=request_data['data']['score_1']
    wa1=int(request_data['data']['walls'])
    print("---------------------------------------------------------------------")
    print(
        "    0a1b2c3d4e5f6g7h8\n",
        "   -----------------\n",
        '0|',board[0:17],'      | Player1:',p1,'\n',
        'a|',board[17:34],'      | Score P1:',sc1,'| Walls:',wa1,'\n',
        '1|',board[34:51],'      | Side: ',side,'| Remaining_moves:',rem,'\n',
        'b|',board[51:68],'      | Player2:',p2,'\n',
        '2|',board[68:85],'      | Score P2:',sc2,'\n',
        'c|',board[85:102],'\n',
        '3|',board[102:119],'\n',
        'd|',board[119:136],'\n',
        '4|',board[136:153],'\n',
        'e|',board[153:170],'\n',
        '5|',board[170:187],'\n',
        'f|',board[187:204],'\n',
        '6|',board[204:221],'\n',
        'g|',board[221:238],'\n',
        '7|',board[238:255],'\n',
        'h|',board[255:272],'\n',
        '8|',board[272:289])
    print("---------------------------------------------------------------------")
    print("turn_token",turn_token)
    print("game_id",game_id)
    print("---------------------------------------------------------------------")
def mindist(request_data):
    i=0
    j=0
    pcs=[0,0,0]
    pci=[0,0,0]
    while i<=288:
        if request_data['data']['board'][i] == request_data['data']['side']:
            pcs[j]=distance(request_data,i)
            pci[j]=i
            if j==2:
                break
            j+=1
        i+=1
    if pcs[0]<=pcs[1] and pcs[0]<=pcs[2]:
        return pci[0]
    elif pcs[1]<=pcs[0] and pcs[1]<=pcs[2]:
        return pci[1]
    elif pcs[2]<=pcs[0] and pcs[2]<=pcs[1]:
        return pci[2]
# Pawns
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
            print("pawnmoveright S",pawnmoveright(request_data,pc))
            return pawnmoveright(request_data,pc)
        elif pawnmovedown(request_data,pc) != None:
            print("pawnmovedown S",pawnmovedown(request_data,pc))
            return pawnmovedown(request_data,pc)
def move(request_data):
    pc=mindist(request_data)
    fromto=movepc(request_data,pc)
    return fromto
# Walls
def mindistop(request_data): 
    i=0
    j=0
    pcs=[0,0,0]
    pci=[0,0,0]
    op="N"
    if request_data['data']['side'] == "N":
        op="S"
    while i<=288:
        if request_data['data']['board'][i] == op:
            pcs[j]=distance(request_data,i)
            pci[j]=i
            if j==2:
                break
            j+=1
        i+=1
    if pcs[0]<=pcs[1] and pcs[0]<=pcs[2]:
        return pci[0]
    elif pcs[1]<=pcs[0] and pcs[1]<=pcs[2]:
        return pci[1]
    elif pcs[2]<=pcs[0] and pcs[2]<=pcs[1]:
        return pci[2]
def wallstop(request_data):
    enemy=mindistop(request_data)
    positionenemy=position(enemy)
    a=int(positionenemy[0])
    b=int(positionenemy[1])
    rds=request_data['data']['side']
    if rds=="S":
        if iswall(request_data,enemy)==1 and positionenemy[1]<8:    return (a+2,b,"h")
        elif iswall(request_data,enemy)==1 and positionenemy[1]==8: return (a+2,b-1,"h")
    if rds=="N":
        if iswall(request_data,enemy)==1 and positionenemy[1]<8:    return (a-2,b,"h")
        elif iswall(request_data,enemy)==1 and positionenemy[1]==8: return (a-2,b-1,"h")
def putwall(request_data):
    print("wallstop:",wallstop(request_data))
    return wallstop(request_data)

