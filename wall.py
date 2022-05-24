from random import randint

def putwall(request_data):
    #return wallstop(request_data)
    return(randint(0, 8),randint(0, 8),'h' if randint(0, 1) == 0 else 'v')
def walldown(request_data,pc):
    print("aca",pc)
    if pc+17>271:
        return None
    elif request_data['data']['board'][pc+17]=="-" or request_data['data']['board'][pc+17]=="*":
        return 2
    elif request_data['data']['board'][pc+17]==" ":
        return 1
def wallup(request_data,pc):
    if pc-17<17:
        return None
    elif request_data['data']['board'][pc-17]=="-" or request_data['data']['board'][pc-17]=="*":
        return 2
    elif request_data['data']['board'][pc-17]==" ":
        return 1
def iswall(request_data,enemy):
    if request_data["data"]["board"][enemy] == "N":
        wall=enemy+17
        if request_data["data"]["board"][wall] == "-" or request_data['data']['board'][wall]=="*":
            return None
        elif request_data["data"]["board"][wall] == " ":
            return 1
    elif request_data["data"]["board"][enemy] == "S":
        wall=enemy-17
        if request_data["data"]["board"][wall] == "-" or request_data['data']['board'][wall]=="*":
            return None
        elif request_data["data"]["board"][wall] == " ":
            return 1

# request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "S", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                  -                S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
# enemy=8
# print(iswall(request_data,enemy))

# request_data={"event": "your_turn", "data": {"remaining_moves": 164.0, "score_1": -19.0, "player_1": "armandogerman@hotmail.com", "score_2": -45.0, "side": "N", "player_2": "armandogerman@hotmail.com", "walls": 7.0, "board": "         N     N                            |         -*- -*-*                | |                *-*-       |     |       -*-*                |   |                *       N       S|       -*- -*-                                                  S           S  ", "turn_token": "ce295c93-6fc0-4477-9852-cb75e878e0ae", "game_id": "53ba8d7e-dafe-11ec-aef0-7ecdf393f9cc"}}
# print(walldown(request_data,172))
