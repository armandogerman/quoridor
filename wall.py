from random import randint
from strategy import *

def putwall(request_data):
    return(randint(0, 8),randint(0, 8),'h' if randint(0, 1) == 0 else 'v')
def walldown(request_data,pc):
    if pc+17>271:
        return None
    elif request_data['data']['board'][pc+17]=="-":
        return 2
    elif request_data['data']['board'][pc+17]==" ":
        return 1
def wallup(request_data,pc):
    if pc-17<17:
        return None
    elif request_data['data']['board'][pc-17]=="-":
        return 2
    elif request_data['data']['board'][pc-17]==" ":
        return 1
