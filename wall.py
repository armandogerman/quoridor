from random import randint

def putwall(request_data):
    return(randint(0, 8),randint(0, 8),'h' if randint(0, 1) == 0 else 'v')
def walldown(request_data,pc):
    if request_data['data']['side']=='N':
        if pc+17>271:
            return None
        elif request_data['data']['board'][pc+17]=="-":
            return 2
        elif request_data['data']['board'][pc+17]==" ":
            return 1
    if request_data['data']['side']=='S':
        if pc+17>271:
            return None
        elif request_data['data']['board'][pc-17]=="-":
            return 2
        elif request_data['data']['board'][pc-17]==" ":
            return 1

