from sqlite3 import PARSE_COLNAMES
from pawn import *
from wall import *
# def strategy(request_data):
#     if select_pawn(request_data) != None:
#         print("select_pawn")
#         return select_pawn(board,actual_turn)
board="  N     N     N                                                                                                         -                                                                                                                                                         S     S     S  "
actual_turn="N"
pcs=2
# def distance(board,actual_turn):
#     acu=0
#     if actual_turn=="N":
#         if pawnmovedown(board,actual_turn) != None:
#             if pawnmoveleft(board,actual_turn) != None:
#                     if pawnmoveright(board,actual_turn) != None:
#                         acu+=1
#                         return pawnmoveup(board,actual_turn)
                            
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

#print(distance(board,actual_turn,pcs))