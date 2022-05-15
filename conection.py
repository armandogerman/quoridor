import asyncio
import json
from random import randint
import sys
import websockets
from strategy import *
from wall import *
from pawn import *

async def send(websocket, action, data):
    message = json.dumps(
        {
            'action': action,
            'data': data,
        }
    )
    print(message)
    await websocket.send(message)


async def start(auth_token):
    uri = "wss://4yyity02md.execute-api.us-east-1.amazonaws.com/ws?token={}".format(auth_token)
    while True:
        try:
            print('connection to {}'.format(uri))
            async with websockets.connect(uri) as websocket:
                await play(websocket)
        except KeyboardInterrupt:
            print('Exiting...')
            break
        except Exception:
            print('connection error!')
            time.sleep(3)


async def play(websocket):
    while True:
        try:
            request = await websocket.recv()
            print(f"< {request}")
            request_data = json.loads(request)
            if request_data['event'] == 'update_user_list':
                pass
            if request_data['event'] == 'gameover':
                pass
            if request_data['event'] == 'challenge':
                # if request_data['data']['opponent'] == 'favoriteopponent':
                await send(
                    websocket,
                    'accept_challenge',
                    {
                        'challenge_id': request_data['data']['challenge_id'],
                    },
                )
            if request_data['event'] == 'your_turn':
                await process_your_turn(websocket, request_data)
        except KeyboardInterrupt:
            print('Exiting...')
            break
        except Exception as e:
            print('error {}'.format(str(e)))
            break  # force login again


async def process_your_turn(websocket, request_data):
    if randint(0, 4) >= 1:
        await process_move(websocket, request_data)
    else:
        await process_wall(websocket, request_data)


async def process_move(websocket, request_data):
        print("************************")
        print('    0    1    2    3    4    5    6    7    8')
        for row in range(9):
            print(row,pawn_board[row][0:9])
        print("   ________________")
        fromto=move(request_data)
        fr=fromto[0]
        to=fromto[1]
        await send(
            websocket,
            'move',
            {
                'game_id': request_data['data']['game_id'],
                'turn_token': request_data['data']['turn_token'],
                'from_row': fr[0],
                'from_col': fr[1],
                'to_row': to[0],
                'to_col': to[1],
            },
        )

async def process_wall(websocket, request_data):
    wally=putwall(request_data)
    row=wally[0]
    col=wally[1]
    orientation=wally[2]

    await send(
        websocket,
        'wall',
        {
            'game_id': request_data['data']['game_id'],
            'turn_token': request_data['data']['turn_token'],
            'row': row,
            'col': col,
            'orientation': orientation
        },
    )

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        auth_token = sys.argv[1]
        asyncio.get_event_loop().run_until_complete(start(auth_token))
    else:
        print('please provide your auth_token')