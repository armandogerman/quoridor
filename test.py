import unittest
from pawn import *
from strategy import *
from wall import *
# pawns    ##
class quoridor_position(unittest.TestCase):
    def test_position0(self):
        actual = position(2)
        esperado = ((0, 2))
        self.assertEqual(actual,esperado)

    def test_position1(self):
        actual = position(288)
        esperado = ((16, 16))
        self.assertEqual(actual,esperado)
    
    def test_position2(self):
        actual = position(36)
        esperado = ((2, 2))
        self.assertEqual(actual,esperado)
class quoridor_identify(unittest.TestCase):
    def test_identify(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        actual = identify(request_data)
        esperado = [2,8,14]
        self.assertEqual(actual,esperado)
class quoridor_pawnmovedown(unittest.TestCase):
    def test_pawnmovedown1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pc=2
        actual = pawnmovedown(request_data,pc)
        esperado = ((0, 2), (2, 2))
        self.assertEqual(actual,esperado)
    def test_pawnmovedown2(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N  -*-                                                                                                                                                                                                                                                              S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pc=2
        actual = pawnmovedown(request_data,pc)
        esperado = None
        self.assertEqual(actual,esperado)   
    def test_pawnmovedown3(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                     S                                                                                                                                                                                                                                             S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pc=2
        actual = pawnmovedown(request_data,pc)
        esperado = ((0, 2), (4, 2))
        self.assertEqual(actual,esperado)
class quoridor_pawnmoveleft(unittest.TestCase):    
    def test_pawnmoveleft1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pc=2
        actual = pawnmoveleft(request_data,pc)
        esperado = ((0, 2), (0, 0))
        self.assertEqual(actual,esperado)
class quoridor_pawnmoveright(unittest.TestCase): 
    def test_pawnmoveright1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pc=2
        actual = pawnmoveright(request_data,pc)
        esperado = ((0, 2), (0, 4))
        self.assertEqual(actual,esperado)
class quoridor_pawnmoveup(unittest.TestCase): 
    def test_pawnmoveup1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "S", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pc=274
        actual = pawnmoveup(request_data,pc)
        esperado = ((16, 2), (14, 2))
        self.assertEqual(actual,esperado)
# walls ****************************************************
class quoridor_walldown(unittest.TestCase): 
    def test_walldown1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pc=2
        actual = walldown(request_data,pc)
        esperado = 1
        self.assertEqual(actual,esperado)
    def test_walldown2(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pc=240
        actual = walldown(request_data,pc)
        esperado = 1
        self.assertEqual(actual,esperado)
# class quoridor_putwall(unittest.TestCase): esta en modo random.
# strategy *************************************************
class quoridor_distance(unittest.TestCase): 
    def test_distance1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pcs=2
        actual = distance(request_data,pcs)
        esperado = 8
        self.assertEqual(actual,esperado)
    def test_distance2(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                          -                                                                                                                                                        S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pcs=2
        actual = distance(request_data,pcs)
        esperado = 9
        self.assertEqual(actual,esperado)
class quoridor_mindist(unittest.TestCase): 
    def test_mindist1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        actual = mindist(request_data)
        esperado = 2
        self.assertEqual(actual,esperado)
    def test_mindist2(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                          -                                                                                                                                                        S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        actual = mindist(request_data)
        esperado = 8
        self.assertEqual(actual,esperado)
class quoridor_move(unittest.TestCase): 
    def test_move1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (0,2),(2,2)
        self.assertEqual(actual,esperado)

if __name__ == "__main__":
    unittest.main()
