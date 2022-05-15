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

def identify(board,actual_turn):
    i=0
    j=0
    pcs=[0,0,0]
    while i<=288:
        if board[i] == actual_turn:
            pcs[j]=i
            j+=1
            if j>2:
                return pcs
        i+=1
        
def pawnmovedown(board,actual_turn):
    i=0
    while i<=288:
        if board[i] == actual_turn:
            if board[i+17] == '-':
                return None            
            elif board[i+34] == ' ': 
                return position(i), position(i+34)
            elif board[i+34] != actual_turn:
                return position(i), position(i+68)              
        i+=1

def pawnmoveleft(board,actual_turn):
    i=0
    while i<=288:
        if board[i] == actual_turn:
            if board[i+1] != '|': 
                if board[i-2] == ' ':
                    return position(i), position(i-2)
        i+=1

def pawnmoveright(board,actual_turn):
    i=0
    while i<=288:
        if board[i] == actual_turn:
            if board[i+1] != '|': 
                if board[i+2] == ' ':
                    return position(i), position(i+2)
        i+=1

def pawnmoveup(board,actual_turn):
    i=0
    while i<=288:
        if board[i] == actual_turn:
            if board[i-17] != '-': 
                if board[i-36] == ' ':
                    return position(i), position(i-34)
        i+=1



# print(identify(board,actual_turn))
