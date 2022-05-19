def position(i):
    for j in range(17):
        col = i-(j*17*2)
        if col<17 and col>=0:
            if col>8:
                return j,col-8
        if col<=8:
            return j,int(col/2)
def index(j,col):
    return j*17+col
def pawnmovedown(request_data,pc):
    if request_data['data']['board'][pc] == request_data['data']['side']:
        if request_data['data']['board'][pc+17] == '-':
            return None            
        elif request_data['data']['board'][pc+34] == ' ':
            return position(pc), position(pc+34)
        elif request_data['data']['board'][pc+34] != request_data['data']['side']:
            if request_data['data']['board'][pc+51] == '-':
                return position(pc), position(pc+70)
            elif request_data['data']['board'][pc+51] == ' ':
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
            return None 
        elif request_data['data']['board'][pc-34] == ' ':
            return position(pc), position(pc-34)
        elif request_data['data']['board'][pc-34] != request_data['data']['side']:
            if request_data['data']['board'][pc-51] == '-':
                return position(pc), position(pc-70)
            elif request_data['data']['board'][pc-51] == ' ':
                return position(pc), position(pc-68)
def movepc(request_data,pc):
    if request_data['data']['side']=="N":
        if pawnmovedown(request_data,pc) != None:
            print("pawnmovedown N")
            return pawnmovedown(request_data,pc)
        elif pawnmoveleft(request_data,pc) != None:
            print("pawnmovedown N")
            return pawnmoveleft(request_data,pc)
        elif pawnmoveright(request_data,pc) != None:
            print("pawnmoveright N")
            return pawnmoveright(request_data,pc)
        elif pawnmoveup(request_data,pc) !=None:
            print("pawnmoveup N")
            return pawnmoveup(request_data,pc)
    if request_data['data']['side']=="S":
        if pawnmoveup(request_data,pc) !=None:
            print("pawnmoveup S")
            return pawnmoveup(request_data,pc)
        elif pawnmoveleft(request_data,pc) != None:
            print("pawnmoveleft S")
            return pawnmoveleft(request_data,pc)
        elif pawnmoveright(request_data,pc) != None:
            return pawnmoveright(request_data,pc)
        elif pawnmoveup(request_data,pc) !=None:
            print("pawnmoveright S")
            return pawnmoveup(request_data,pc)
        elif pawnmovedown(request_data,pc) != None:
            print("pawnmovedown S")
            return pawnmovedown(request_data,pc)