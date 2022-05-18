# from turtle import clear

# request_data={
#     "event": "your_turn", 
#     "data": {   
#         "player_2": "armandogerman@hotmail.com",
#         "score_1": 5.0,
#         "walls": 10.0, 
#         "player_1": "armandogerman@hotmail.com", 
#         "score_2": 2.0, 
#         "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ",
#         "side": "S", 
#         "remaining_moves": 197.0, 
#         "turn_token": "d20892c5-e548-4008-ad1d-14fc0d331ea1", 
#         "game_id": "4e60cb66-d0c9-11ec-aef0-7ecdf393f9cc"    
#     }
# }


board="  N     N     N                     S                                                                                                                                                                                                                                             S     S     S  "
actual_turn="N"

def position(i):                #this function transform the chessboard and returns (x,y) coordinates
    for j in range(0, 17):
        col = i-(j*17)
        if col<17 and col>=0:
            return j,col

def index(j,col):                #this function transform the chessboard and returns (x,y) coordinates
    return j*17+col

def identify(request_data):
    i=0
    j=0
    pcs=[0,0,0]
    while i<=288:
        if request_data['data']['board'][i] == request_data['data']['side']:
            pcs[j]=i
            if j==2:
                return pcs
            j+=1
        i+=1

def pawnmovedown(request_data,pc):
    if request_data['data']['board'][pc] == request_data['data']['side']:
        if request_data['data']['board'][pc+17] == '-':
            return None            
        elif request_data['data']['board'][pc+34] == ' ': 
            return position(pc), position(pc+34)
        elif request_data['data']['board'][pc+34] != actual_turn:
            return position(pc), position(pc+68)              

def pawnmoveleft(request_data,pc):
    if request_data['data']['board'][pc] == request_data['data']['side']:
        if request_data['data']['board'][pc+1] != '|': 
            if request_data['data']['board'][pc-2] == ' ':
                return position(pc), position(pc-2)

def pawnmoveright(request_data,pc):
    if request_data['data']['board'][pc] == request_data['data']['side']:
        if request_data['data']['board'][pc+1] != '|': 
            if request_data['data']['board'][pc+2] == ' ':
                return position(pc), position(pc+2)

def pawnmoveup(request_data,pc):
    if request_data['data']['board'][pc] == request_data['data']['side']:
        if request_data['data']['board'][pc-17] != '-': 
            if request_data['data']['board'][pc-34] == ' ':
                return position(pc), position(pc-34)

def movepc(request_data,pc):
    if request_data['data']['side']=="N":
        if pawnmovedown(request_data,pc) != None:
            return pawnmovedown(request_data,pc)
        elif pawnmoveleft(request_data,pc) != None:
            return pawnmoveleft(request_data,pc)
        elif pawnmoveright(request_data,pc) != None:
            return pawnmoveright(request_data,pc)
        elif pawnmoveup(request_data,pc) !=None:
            return pawnmoveup(request_data,pc)


# print(identify(board,actual_turn))
