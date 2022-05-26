from random import randint

# def putwall(request_data):
#     return wallstop(request_data)
    # w=(randint(0, 8),randint(0, 8),'h' if randint(0, 1) == 0 else 'v')
    # print(w)
    # return w
def walldown(request_data,pc):
    if pc+17>271:
        return None
    if pc+51<=288:
        if request_data['data']['board'][pc+51]=="-" or request_data['data']['board'][pc+51]=="*" or request_data['data']['board'][pc+51]=="|":
            return 3
    if request_data['data']['board'][pc+17]=="-" or request_data['data']['board'][pc+17]=="*" or request_data['data']['board'][pc+17]=="|":
        return 2
    elif request_data['data']['board'][pc+17]==" ":
        return 1

def wallup(request_data,pc):
    if pc-17<17:
        return None
    if pc-51>=0:
        if request_data['data']['board'][pc-51]=="-" or request_data['data']['board'][pc-51]=="*" or request_data['data']['board'][pc-51]=="|":
            return 3
    if request_data['data']['board'][pc-17]=="-" or request_data['data']['board'][pc-17]=="*" or request_data['data']['board'][pc-17]=="|":
        return 2
    elif request_data['data']['board'][pc-17]==" ":
        return 1
def iswall(request_data,enemy):
    if request_data["data"]["board"][enemy] == "N":
        wall=enemy+17
        c1=request_data["data"]["board"][wall]
        c2=request_data["data"]["board"][wall+1]
        c3=request_data["data"]["board"][wall+2]
        if c1=="-" or c1=="*" or c1=="|" or c2=="-" or c2=="*" or c2=="|" or c3=="-" or c3=="*" or c3=="|":
            return None
        elif request_data["data"]["board"][wall] == " ":
            return 1
    elif request_data["data"]["board"][enemy] == "S":
        wall=enemy-17
        c1=request_data["data"]["board"][wall]
        c2=request_data["data"]["board"][wall+1]
        c3=request_data["data"]["board"][wall+2]
        if c1=="-" or c1=="*" or c1=="|" or c2=="-" or c2=="*" or c2=="|" or c3=="-" or c3=="*" or c3=="|":
            return None
        elif request_data["data"]["board"][wall] == " ":
            return 1

request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
pc=2
print(walldown(request_data,pc))