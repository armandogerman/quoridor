# board="              N                           N                           N                                            |                *                |                               S     S     S                              |                *                |     "
# board="  N     N     N                     S                                                                                                                                                                                                                                             S     S     S  "
# board="  N     N     N                                                                                                                                                                                                                                                                   S     S     S  "

# print("************************")
# print("    0a1b2c3d4e5f6g7h8\n",'0|',board[0:16],'\n','a|', board[17:33],'\n','1|',board[34:50],'\n','b|',board[51:67],'\n','2|',board[68:84],'\n','c|',board[85:101],'\n','3|',board[102:118],'\n','d|',board[119:135],'\n','4|',board[136:152],'\n','e|',board[153:169],'\n','5|',board[170:186],'\n','f|',board[187:203],'\n','6|',board[204:220],'\n','g|',board[221:237],'\n','7|',board[238:254],'\n','h|',board[255:271],'\n','8|',board[272:288])
# print("************************")

# board = "  N     N     N                                                                                                          -                                                                                                                                                        S     S     S  "
# actual_turn = "N"
# pc=104

# print(walldown(board,actual_turn,pc))

from random import randint

def putwall(request_data):
    return(randint(0, 8),randint(0, 8),'h' if randint(0, 1) == 0 else 'v')

def walldown(request_data,pc):
    if pc+17>271:
        return None
    elif request_data['data']['board'][pc+17]=="-":
        return None
    elif request_data['data']['board'][pc+17]==" ":
        return 1



