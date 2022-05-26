from random import randint

def walldown(request_data,pc):
    if pc+17>271:
        return None
    if pc+51<=288:
        if request_data['data']['board'][pc+51]=="-" or request_data['data']['board'][pc+51]=="*" or request_data['data']['board'][pc+51]=="|":
            return 3
    if request_data['data']['board'][pc+17]=="-" or request_data['data']['board'][pc+17]=="*" or request_data['data']['board'][pc+17]=="|":
        if request_data['data']['board'][pc+16]=="-" or request_data['data']['board'][pc+16]=="*" or request_data['data']['board'][pc+16]=="|":
            if request_data['data']['board'][pc+18]=="-" or request_data['data']['board'][pc+18]=="*" or request_data['data']['board'][pc+18]=="|":
                return 4
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
        if request_data['data']['board'][pc-16]=="-" or request_data['data']['board'][pc-16]=="*" or request_data['data']['board'][pc-16]=="|":
            if request_data['data']['board'][pc-18]=="-" or request_data['data']['board'][pc-18]=="*" or request_data['data']['board'][pc-18]=="|":
                return 4
        return 2
    elif request_data['data']['board'][pc-17]==" ":
        return 1
def iswall(request_data,enemy):
    c1=request_data["data"]["board"][wall]
    c2=request_data["data"]["board"][wall+1]
    c3=request_data["data"]["board"][wall+2]
    if request_data["data"]["board"][enemy] == "N":
        wall=enemy+17
        if c1=="-" or c1=="*" or c1=="|" or c2=="-" or c2=="*" or c2=="|" or c3=="-" or c3=="*" or c3=="|":
            return None
        elif request_data["data"]["board"][wall] == " ":
            return 1
    elif request_data["data"]["board"][enemy] == "S":
        wall=enemy-17
        if c1=="-" or c1=="*" or c1=="|" or c2=="-" or c2=="*" or c2=="|" or c3=="-" or c3=="*" or c3=="|":
            return None
        elif request_data["data"]["board"][wall] == " ":
            return 1
