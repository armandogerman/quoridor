from re import A
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
            pcs=pcs+34
        return acu
    if request_data['data']['side']=="S":
        acu=0
        while pcs<=254:
            if walldown(request_data,pcs)==1:
                acu+=1
            elif walldown(request_data,pcs)==2:
                acu+=2
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
        '0|',board[0:16],'      | Player1:',p1,'\n',
        'a|',board[17:33],'      | Score:',sc1,'| Walls:',wa1,'\n',
        '1|',board[34:50],'      | Side: ',side,'| Remaining_moves:',rem,'\n',
        'b|',board[51:67],'      | Player2:',p2,'\n',
        '2|',board[68:84],'      | Score:',sc2,'\n',
        'c|',board[85:101],'\n',
        '3|',board[102:118],'\n',
        'd|',board[119:135],'\n',
        '4|',board[136:152],'\n',
        'e|',board[153:169],'\n',
        '5|',board[170:186],'\n',
        'f|',board[187:203],'\n',
        '6|',board[204:220],'\n',
        'g|',board[221:237],'\n',
        '7|',board[238:254],'\n',
        'h|',board[255:271],'\n',
        '8|',board[272:288])
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
    print("mindist -> pcs",pcs,"pci",pci)
    print(request_data['data']['board'][i],"lalalala",request_data['data']['side'])
    a=str(pcs[0])
    b=str(pcs[1])
    c=str(pcs[2])
    if a<=b:
        if a<=c:
            return a
        elif a>c:
            return c
    elif b<=c:
            return b
    elif b>c:
        return c
def move(request_data):
    pc=mindist(request_data)
    fromto=movepc(request_data,pc)
    print("************ FROM: ",fromto[0],"-> TO:",fromto[1]," **************")
    return fromto
