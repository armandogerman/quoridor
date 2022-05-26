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

def pawnmovedown(request_data,pc):
    s=request_data['data']['side']
    pdb=request_data['data']['board']
    if pc+17<=288:
        if pdb[pc+17]=='-' or pdb[pc+17]=='*' or pdb[pc+17]=='|':   return None
    if pc+51<=288:
        if pdb[pc+51]=='-' or pdb[pc+51]=='*' or pdb[pc+51]=='|':   return None  
    if pc+34<=288:
        if pdb[pc+34]==' ':                 return position(pc), position(pc+34)
        elif pdb[pc+34]!=s:
            if pc+68<=288:
                if pdb[pc+68]==' ':         return position(pc), position(pc+68)
            if pc+36<=288:
                if pdb[pc+36]==' ':
                    a=position(pc)
                    b=position(pc+36)
                    if a[1]==b[1]+1 or a[1]==b[1]-1:                return a, b
            if pc+32<=288:               
                if pdb[pc+32]==' ':
                    a=position(pc)
                    b=position(pc+32)
                    if a[1]==b[1]+1 or a[1]==b[1]-1:                return a, b

def pawnmoveleft(request_data,pc):
    rdb=request_data['data']['board']
    rds=request_data['data']['side']
    if rdb[pc-1] != '|': 
        if rdb[pc-2] == ' ':
            if rds=='S':
                if position(pc-2)==None:    return None
                if rdb[pc-19]==' ':         return position(pc), position(pc-2)
            elif rds=='N':
                if position(pc-2)==None:    return None
                if rdb[pc+19]==' ':         return position(pc), position(pc-2)
    if rdb[pc-1] == '|':
        return None

def pawnmoveright(request_data,pc):
    rdb=request_data['data']['board']
    rds=request_data['data']['side']
    if rdb[pc+1] != '|': 
        if rdb[pc+2] == ' ':
            if rds=='S':
                if position(pc+2)==None:    return None
                if rdb[pc-15]==' ':         return position(pc), position(pc+2)
            elif rds=='N':
                if position(pc+2)==None:    return None
                if rdb[pc+19]==' ':         return position(pc), position(pc+2)
    if rdb[pc-1] == '|':
        return None

def pawnmoveup(request_data,pc):
    rdb=request_data['data']['board']
    s=request_data['data']['side']
    if pc-34>=0:
        if rdb[pc-17]=='-' or rdb[pc-17]=='*' or rdb[pc-17]=='|':   return None
        if rdb[pc-17]==' ' and rdb[pc-34]==' ': return position(pc), position(pc-34)
    if pc-34>=0:
        if rdb[pc-34]==' ':                 return position(pc), position(pc-34)
        elif rdb[pc-34]!=s:
            if pc-68>=0:
                if rdb[pc-68]==' ':         return position(pc), position(pc-68)
            if pc-36>=0:
                if rdb[pc-36]==' ':
                    a=position(pc)
                    b=position(pc-36)
                    if a[1]==b[1]+1 or a[1]==b[1]-1:                return a, b
            if pc-32>=0:               
                if rdb[pc-32]==' ':
                    a=position(pc)
                    b=position(pc-32)
                    if a[1]==b[1]+1 or a[1]==b[1]-1:                return a, b
    if pc-51>=0: # 2
        if rdb[pc-51]=='-' or rdb[pc-51]=='*' or rdb[pc-51]=='|':   return None

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
