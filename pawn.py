def position(i):
  for j in range(17):
    col = i-(j*34)
    acu=0
    if col<=17:
      while col>=0:
        if col==0:
          return j,acu
        elif col>0:
          col-=2
          acu+=1
def index(j,col):
    return j*17+col
def pawnmovedown(request_data,pc):
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
    if request_data['data']['board'][pc-17] == '-':
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
            print("pawnmoveright",pawnmoveright(request_data,pc))
            return pawnmoveright(request_data,pc)
        elif pawnmoveup(request_data,pc) !=None:
            print("pawnmoveup S",pawnmoveup(request_data,pc))
            return pawnmoveup(request_data,pc)
        elif pawnmovedown(request_data,pc) != None:
            print("pawnmovedown S",pawnmovedown(request_data,pc))
            return pawnmovedown(request_data,pc)

