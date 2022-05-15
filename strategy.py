from pawn import *
from wall import *
# def strategy(request_data):
#     if select_pawn(request_data) != None:
#         print("select_pawn")
#         return select_pawn(board,actual_turn)
board="  N     N     N                                                                                                         -                                                                                                                                                         S     S     S  "
actual_turn="N"
pcs=2
request_data={"event": "your_turn", "data": {"walls": 9.0, "score_1": -47.0, "score_2": 126.0, "side": "N", "remaining_moves": 188.0, "player_2": "agustin1997aguero@gmail.com", "player_1": "armandogerman@hotmail.com", "board": "  N     N     N                               |                *       S        |                        S     S  ", "turn_token": "783f585d-22b5-4b72-92ab-81ba238a7f0e", "game_id": "d99b9ab6-d485-11ec-aef0-7ecdf393f9cc"}}
                        
def distance(board,actual_turn,pcs):
    if actual_turn=="N":
        acu=0
        while pcs<=254:
            if walldown(board,actual_turn,pcs)==1:
                acu+=1
            elif walldown(board,actual_turn,pcs)==None:
                acu+=2
            pcs=pcs+34
        return acu
            
def mindist(board,actual_turn):
    pcs=identify(board,actual_turn)
    a=distance(board,actual_turn,pcs[0])
    b=distance(board,actual_turn,pcs[1])
    c=distance(board,actual_turn,pcs[2])
    if a<=b and a<=c:
        return pcs[0]
    elif b<=a and b<=c:
        return pcs[1]
    elif c<=a and c<=b:
        return pcs[2]

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
    print("************************")
    print(
        "    0a1b2c3d4e5f6g7h8\n",
        '0|',board[0:16],'      | Player1:',p1,'\n',
        'a|',board[17:33],'      | Walls:',wa1,'| Score:',sc1,'\n',
        '1|',board[34:50],'      | side: ',side,'| Remaining_moves:',rem,'\n',
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
    print("************************************************")
    print("turn_token",turn_token)
    print("game_id",game_id)
    print("************************************************")

# print(imprimir(request_data))